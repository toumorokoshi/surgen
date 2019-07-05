import attr

ResultStatus = {"PASS": "PASS", "FAIL": "FAIL", "SKIP": "SKIP"}


@attr.s(frozen=True)
class Result(object):
    procedure = attr.ib()
    status = attr.ib()

    def __str__(self):
        return "procedure: {0}, status: {1}".format(self.procedure, self.status)


class Results(list):
    """ stores a list of results. """

    def __init__(self):
        super(Results, self).__init__()
        self._by_status = {}
        for r in ResultStatus.values():
            self._by_status[r] = 0

    def __str__(self):
        return "\n".join(list(str(e) for e in self))

    def short_summary(self) -> str:
        """
        return a shortened summary that only
        includes passed procedures
        """
        return "\n".join((str(result) for result in self if result.status == "PASS"))

    def add(self, result):
        super(Results, self).append(result)
        self._by_status[result.status] += 1

    @property
    def count_by_status(self):
        return self._by_status
