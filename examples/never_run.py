from surgen import Procedure


class NeverRun(Procedure):

    def operate(self):
        raise Exception("I RAN!!!")

    def should_not_run(self):
        return "this should always skip."
