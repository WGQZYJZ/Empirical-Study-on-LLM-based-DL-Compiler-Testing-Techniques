
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v2 + 1


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 4)
__output__  = m(x1)