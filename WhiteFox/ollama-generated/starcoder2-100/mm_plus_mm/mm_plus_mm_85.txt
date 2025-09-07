
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x2, x3):
        v4  = torch.mm(x2, x3)
        v7 = self.linear(v4)
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(50, 10)
x2 = torch.randn(10, 100)
x3 = torch.randn(100, 1000)
__output__  = m(x1, x2, x3)

