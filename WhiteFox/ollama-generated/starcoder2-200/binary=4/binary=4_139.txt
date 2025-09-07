
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 5)
 
    def forward(self, x):
        v1 = self.linear(x) + torch.randn_like(v1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x = torch.rand(234, 100)
__output__  = m(x)