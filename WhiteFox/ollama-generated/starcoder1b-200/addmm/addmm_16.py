
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(32, 64)
 
    def forward(self, x1, inp=10):
        m = self.m(x1) + inp
        return m


# Inputs to the model
input1 = torch.randn(10, 10)
