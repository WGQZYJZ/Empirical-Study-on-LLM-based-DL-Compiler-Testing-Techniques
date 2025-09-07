
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(8, 16)
        self.sigm = torch.nn.Sigmoid()
 
    def forward(self, x2):
        v1 = self.lin(x2)
        v2 = self.sigm(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x2 = torch.randn(1, 8, 64)
