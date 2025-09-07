
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(32, 48)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + other # other is not used here
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
other = torch.randn(48,)


# Inputs to the model