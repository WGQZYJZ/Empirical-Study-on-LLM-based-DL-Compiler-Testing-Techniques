
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 8, bias=False)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(256, 30)
__output__  = m(x1)


