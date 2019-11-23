import os
import subprocess
from subprocess import PIPE
from ipykernel.kernelbase import Kernel


class MicroPythonRepl:

    def __init__(self):
        self.available = MicroPythonRepl._is_micropython_defined()

    @staticmethod
    def _is_micropython_defined() -> bool:
        if os.environ['MICROPYPATH'] is not None:
            return True
        raise Exception("MICROPYPATH env variable is not defined."
                        "Cannot run micropython's kernel.")

    @staticmethod
    def _decode_result(result_as_bytes: bytes) -> str:
        return result_as_bytes.decode()

    def run_code(self, code: str) -> str:
        result = subprocess.run(['micropython', '-c', code], stdout=PIPE, stderr=PIPE)
        if result.returncode == 0:
            return MicroPythonRepl._decode_result(result.stdout)
        return MicroPythonRepl._decode_result(result.stderr)


class MicroPythonKernel(Kernel):

    implementation = 'MicroPython'
    implementation_version = '0.0.1'
    language = 'micropython'
    language_info = {
        'name': 'unix_micropython_kernel',
        'mimetype': 'text/plain',
        'file_extension': '.py',
    }
    banner = "Jupyter kernel for MicroPython's UNIX port"

    @property
    def micropython_repl(self) -> MicroPythonRepl:
        return MicroPythonRepl()

    def do_clear(self):
        pass

    def do_apply(self, content, bufs, msg_id, reply_metadata):
        pass

    def do_execute(self,
                   code,
                   silent,
                   store_history=True,
                   user_expressions=None,
                   allow_stdin=False):
        if not silent:

            result = self.micropython_repl.run_code(code)

            stream_content = {'name': 'stdout', 'text': result}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            # The base class increments the execution count
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }
