
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.linear(x1) # Replace `torch.linear` with `torch.nn.Linear(in_features=4096, out_features=32)`
        v2  = self._other + v1
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(56, 4096)


# Input tensor for the first run
x1_first_run = 5 * x1 + 3
 
