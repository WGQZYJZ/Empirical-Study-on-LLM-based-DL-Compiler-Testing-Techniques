
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.lin(x1) 
        v2 = sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m = Model()
__output__  = m(__input__)

