
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        if isinstance(other, int):
            v2 = v1 + other
        elif isinstance(other, float):
            v2 = v1 - other
        else:
            v2  = v1 / 2
        return v2


# Initializing the model with the keyword argument `other` set to `10`:
m = Model(other=10)

# Inputs to the model: 
x1  = torch.randn(1, 3) # Input tensor of shape (batch_size, input_dim) or (input_dim).

# Output from the model: 
__output__  = m(x1, other=None)

