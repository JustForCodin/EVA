class EVADecisionEvaluator:
    decision_space: list

    def __init__(self, decision_space: list):
        self.decision_space = decision_space
    
    def decision_forward_pass(self, decision_space):
        R = []
        for i in range(len(self.decision_space)):
            R.append(self.decision_space[i]-self.decision_space[i-1])
        return max(R)    

    def decision_backward_pass(self, decision_space):
        R = []
        for i in range(len(self.decision_space)):
            R.append(self.decision_space[i-1]-self.decision_space[i])
        return max(R)

class EVAMostRationalDecisionFinder:
    @staticmethod
    def MRDS(self):
        reward = 0
        N = 10000
        for _ in range(N):
            if EVADecisionEvaluator([1, 3, 2, 4, 9, 0, 5, 6]).decision_forward_pass() >= 0:
                reward += 10
            reward -= 15
