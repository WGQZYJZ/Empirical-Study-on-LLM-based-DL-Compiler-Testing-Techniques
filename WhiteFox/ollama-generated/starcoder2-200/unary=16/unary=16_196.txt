
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(512, 10)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        return relu_(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3,512)

__output__  = m(x1)

