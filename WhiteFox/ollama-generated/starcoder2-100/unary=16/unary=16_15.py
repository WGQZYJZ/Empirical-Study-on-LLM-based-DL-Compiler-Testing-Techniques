
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(25600, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.relu(v1) 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8000, 25600)
__output__  = m(x1)

