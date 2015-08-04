"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from django.template import Context, Template


class DailyMotionXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    display_name = String(display_name="Display Name",
        default="DailyMotion",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    url = String(display_name="PDF URL",
        default="https://www.dailymotion.com/embed/video/x2men6q",
        scope=Scope.content,
        help="The URL for your PDF.")

    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))


    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the DailyMotionXBlock, shown to students
        when viewing courses.
        """
        context = {
            'display_name': self.display_name,
            'url': self.url,
        }
        html = self.render_template('static/html/dm_view.html', context)
        
        frag = Fragment(html)
        frag.add_css(self.load_resource("static/css/dailymotion.css"))
        frag.add_javascript(self.load_resource("static/js/src/dm_view.js"))
        frag.initialize_js('DailyMotionXBlockInitView')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    # @XBlock.json_handler
    # def increment_count(self, data, suffix=''):
    #     """
    #     An example handler, which increments the data.
    #     """
    #     # Just to show data coming in...
    #     assert data['hello'] == 'world'

    #     self.count += 1
    #     return {"count": self.count}

    # # TO-DO: change this to create the scenarios you'd like to see in the
    # # workbench while developing your XBlock.
    # @staticmethod
    # def workbench_scenarios():
    #     """A canned scenario for display in the workbench."""
    #     return [
    #         ("DailyMotionXBlock",
    #          """<vertical_demo>
    #             <dailymotion/>
    #             <dailymotion/>
    #             <dailymotion/>
    #             </vertical_demo>
    #          """),
    #     ]
    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'url': self.url
        }
        html = self.render_template('static/html/dm_edit.html', context)
        
        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/dm_edit.js"))
        frag.initialize_js('DailyMotionXBlockInitEdit')
        return frag

    @XBlock.json_handler
    def save_dm(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.url = data['url']
        
        return {
            'result': 'success',
        }
