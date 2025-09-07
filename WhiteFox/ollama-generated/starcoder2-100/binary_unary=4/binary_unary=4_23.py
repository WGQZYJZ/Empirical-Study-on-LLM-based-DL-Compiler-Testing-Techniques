
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v0 = self.linear(x1) + other 
        v2 = torch.relu(v0)

        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3,64)

