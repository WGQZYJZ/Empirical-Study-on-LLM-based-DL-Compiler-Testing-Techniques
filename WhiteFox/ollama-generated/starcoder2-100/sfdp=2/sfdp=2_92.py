
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(784, 600)

    def forward(self, x1):
        v1 = torch.matmul(x1, self.qk(x1).transpose(-2, -1))
        v2 = qk * 53.931343892
        return v2
# Initializing the model
m = Model()


# Inputs to the model