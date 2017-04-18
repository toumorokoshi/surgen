import os
from surgen import Procedure


class KeepScope(Procedure):

    def operate(self):
        self.log(os.path.dirname(__file__))
