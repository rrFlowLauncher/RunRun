import os.path
import subprocess
from flox import Flox

INITIAL_KEY = "Open Configuration"

class RunRun(Flox):
    def query(self, query):
        if not self.settings:
            self.initial_settings()
        if query == INITIAL_KEY:
            self.add_item(
                title=INITIAL_KEY,
                subtitle="{} - {}".format(self.action_keyword, INITIAL_KEY),
                method=self.open_settings_folder
            )
        else:
            for key, value in self.settings.items():
                self.add_item(
                    title=key,
                    subtitle=value,
                    method=self.change_query,
                    parameters=[value],
                    dont_hide=True
                )

    def initial_settings(self):
        initial_settings = {INITIAL_KEY: "{} {}".format(self.action_keyword, INITIAL_KEY)}
        self.settings.update(initial_settings)

    def context_menu(self, data):
        pass

    def open_settings_folder(self):
        settings_path = self.settings_path.rsplit(os.path.sep, 1)[0]
        subprocess.Popen("explorer {}".format(settings_path), shell=True)


if __name__ == "__main__":
    run_run = RunRun()
    run_run.run()