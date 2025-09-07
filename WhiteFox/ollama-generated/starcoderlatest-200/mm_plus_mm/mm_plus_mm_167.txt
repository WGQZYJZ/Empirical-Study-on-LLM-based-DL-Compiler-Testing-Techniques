
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 2)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1)
        return self.linear2(v2 + v3)


# Initializing the model
m = Model()


# Inputs to the model
__input1__ = torch.randn(1, 2, 64, 64)
__input2__ = torch.randn(1, 4, 64, 64)
__input3__ = torch.randn(1, 8, 64, 64)
__input4__ = torch.randn(1, 16, 64, 64)
