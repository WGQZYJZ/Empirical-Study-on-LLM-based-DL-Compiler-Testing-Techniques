
class Model(torch.nn.Module):
    def __init__(self, opt):
        super().__init__()
        self.opt = opt
        self.linear 1 = torch.nn.Linear(2, 2)
        self.linear 2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = self.opt(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 3)
