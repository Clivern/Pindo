# MIT License
#
# Copyright (c) 2021 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
from pindo.runner import Runner
from multiprocessing import Process, Manager

def f(engine, output):
    try:
        engine.setup()
        r = engine.run()
    except Exception as e:
        output['result'] = {}
        return

    output['result'] = r


if __name__ == '__main__':
    code = """
    <?php
    echo "Hello World";
    """

    php_code = Runner.php(code, "7.4")

    engine = Runner.docker(php_code)

    manager = Manager()
    out = manager.dict()

    p = Process(target=f, args=(engine, out))
    p.start()
    p.join(timeout=30)
    p.terminate()

    if p.exitcode is None:
        engine.cleanup()
        print(out)
        print(f'Oops, {p} timeouts!')

    if p.exitcode == 0:
        engine.cleanup()
        print(out)
        print(f'{p} finished in less than 30 seconds!')
