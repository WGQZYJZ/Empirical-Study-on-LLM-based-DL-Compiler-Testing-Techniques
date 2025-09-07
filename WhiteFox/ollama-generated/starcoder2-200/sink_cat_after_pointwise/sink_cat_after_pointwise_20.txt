
class Model(torch.nn.Module):
    def __init__(self, num=50):
        super().__init__()

        self.f1  = torch.nn.Sequential()
        self.f2  = torch.nn.Sequential()

        for _ in range(num):
            self.f1.add_module('b1', torch.nn.Flatten())

    def forward(self, x1, x2):
        v0 = torch.cat([x1, x2], dim=...)
        v3  = self.f1(v0)

        v4  = torch.nn.functional.tanh(v3)
        return v4

# Initializing the model
m  = Model()

# Inputs to the model: 4 input tensors, and an additional placeholder tensor. This input is expected by the model.
x1  = torch.randn(8, 2, 2)
x2  = torch.randn(7, 3, 5)
x3  = torch.randn()
__output__   = m(x1, x2)

