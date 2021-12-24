class EVADecision2D:
    d: float 
    f: float 

    def __init__(self, d, f) -> None:
        self.d = d
        self.f = f

class EVADecisionEvaluator:
    decision_space: list

    def __init__(self, decision_space: list):
        self.decision_space = decision_space
    
    def decision_forward_pass(self):
        R = []
        for i in range(len(self.decision_space)):
            R.append(self.decision_space[i]-self.decision_space[i-1])
        return min(R)    

    def decision_backward_pass(self):
        R = []
        for i in range(len(self.decision_space)):
            R.append(self.decision_space[i-1]-self.decision_space[i])
        return min(R)

    def decision_forward_pass_2d(self):
        R = []
        for i in range(len(self.decision_space)):
            R.append(
                [
                    self.decision_space[i].d - self.decision_space[i-1].d,
                    self.decision_space[i].f - self.decision_space[i-1].f
                ] 
            )
        return min(R)

    def decision_backward_pass_2d(self):
        R = []
        for i in range(len(self.decision_space)):
            R.append(
                [
                    self.decision_space[i-1].d - self.decision_space[i].d,
                    self.decision_space[i-1].f - self.decision_space[i].f
                ] 
            )
        return min(R)

evaluator = EVADecisionEvaluator([
    EVADecision2D(9.0, 3.0), EVADecision2D(3.0, 1.0),
    EVADecision2D(0.5, 1.0), EVADecision2D(4.0, 2.0)
])

print(evaluator.decision_forward_pass_2d())
