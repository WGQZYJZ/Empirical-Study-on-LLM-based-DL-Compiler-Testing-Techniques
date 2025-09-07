
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(300, 1024)
