from surgen import Procedure


class DoNothing(Procedure):

    def operate(self):
        # using self.log ensures proper formatting.
        self.log("hello world!")
