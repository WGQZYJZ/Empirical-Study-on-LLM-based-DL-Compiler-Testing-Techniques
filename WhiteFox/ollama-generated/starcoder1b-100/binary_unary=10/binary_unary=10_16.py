
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 12)
 
    def forward(self, x1, x2=None):
        v1 = self.linear(x1) + x2
        v3 = torch.relu(v1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
__input__  = torch.randn(4, 5)
x1, x2  = __input__, None
