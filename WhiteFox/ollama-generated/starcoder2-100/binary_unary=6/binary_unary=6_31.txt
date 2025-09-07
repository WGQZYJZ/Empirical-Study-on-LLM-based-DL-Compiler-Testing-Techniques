
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(512, 84)

    def forward(self, x0):
        v0  = self.lin(x0)

        v1  = other
        v2  = v0 - v1 # subtract 'other' from the output of the linear transformation
        v3  = torch.relu(v2) 
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1,512)
__output__  = m(x0)