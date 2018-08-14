
## relm.core.template
import os

def func_template(self):
    self.debug()

    if not os.path.isfile('email.template'):

                templateData = '''From: $sender
    To: $to
    Subject: RELMON $name has been updated
    Mime-Version: 1.0
    Content-Type: text/html

    Monitored software <strong>$name</strong> has been updated from version <strong>$version_old</strong> to version <strong>$version_new</strong>.
    <br/>
    You can find more information <a href="$url">here</a>.'''

                with open('email.template', 'w') as templatefile:
                    templatefile.write(templateData)
