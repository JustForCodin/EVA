class EVADecision:
    d: float  # decision rationality
    l: float  # decision label (e.g 0, 1 or -1)

    def __init__(self, d, l) -> None:
        self.d = d
        self.l = l


class EVADecisionEvaluator:
    decision_space: list

    def __init__(self, decision_space: list):
        self.decision_space = decision_space

    def decision_forward_pass(self) -> list :
        R = []
        for i in range(len(self.decision_space)):
            R.append(self.decision_space[i] - self.decision_space[i - 1])
        return min(R)

    def decision_backward_pass(self) -> list:
        R = []
        for i in range(len(self.decision_space)):
            R.append(self.decision_space[i - 1] - self.decision_space[i])
        return min(R)

    def decision_forward_pass_2d(self) -> list:
        R = []
        for i in range(len(self.decision_space)):
            R.append(
                [
                    self.decision_space[i].d - self.decision_space[i - 1].d,
                    self.decision_space[i].l
                ]
            )
        return min(R)

    def decision_backward_pass_2d(self) -> list:
        R = []
        for i in range(len(self.decision_space)):
            R.append(
                [
                    self.decision_space[i - 1].d - self.decision_space[i].d,
                    self.decision_space[i].l
                ]
            )
        return min(R)
