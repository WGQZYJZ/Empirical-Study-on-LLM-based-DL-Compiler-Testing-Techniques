
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(10, 2)
 
    def forward(self, x1, inp):
        v1 = self.matmul(x1).mm(inp)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(20, 10)
inp = torch.randn(10, 3)
