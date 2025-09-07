
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):  # other is defined here!
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model with a constant tensor as the keyword argument
m = Model()
constant_tensor  = torch.randn(7, 7)

# Inputs to the model
x1  = torch.randn(5, 5)
