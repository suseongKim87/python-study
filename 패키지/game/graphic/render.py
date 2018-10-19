"""
import 패키지.game.sound.echo as echo

def render_test():
    print("render")
    echo.echo_test()

render_test()
"""
#위와 같은 import 방식. ( .. 은 부모를 의미.)
# .. 을 인터프린터에서 사용하는 경우에는 error
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()

