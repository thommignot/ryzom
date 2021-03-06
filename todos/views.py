from ryzom.views import View
from todos.components.base import Base
from todos.components.home import Welcome
from todos.components.tasks import Tasklist, Taskform


class Layout(View):
    def oncreate(self, url):
        self.url = url
        self.content = Base(self)

    def onurl(self, url):
        self.url = url
        if url == 'todos':
            self.reactive('main-container', [Tasklist(), Taskform()])
        else:
            self.reactive('main-container', [Welcome()])
        return True

    def render(self):
        return [self.content.to_obj()]
