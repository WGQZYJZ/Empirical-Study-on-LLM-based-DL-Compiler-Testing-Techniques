
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(3072, 1536)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3072)
__output__  = m(x1) 
