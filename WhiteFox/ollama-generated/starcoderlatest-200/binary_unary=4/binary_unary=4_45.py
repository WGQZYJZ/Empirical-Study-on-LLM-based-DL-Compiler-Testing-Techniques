
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 1024)
 
    def forward(self, x1, other):
        v1 = self.linear(x1.view(-1))
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.ones_like(v1).type_as(x1) # Generate an input tensor with same shape and data type as v1. This is used for comparison later.
