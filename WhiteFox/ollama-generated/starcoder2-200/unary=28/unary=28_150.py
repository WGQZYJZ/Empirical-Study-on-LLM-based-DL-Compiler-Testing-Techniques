
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 2)

    def forward(self, x1):
        v1  = self.linear(x1)
        v3  = v2 * min_value # Clamp to minimum value
        v4  = v3 + max_value - min_value # Clamp to maximum minus the minimum values
        return v4


# Initializing model
m = Model()

# Inputs to the model. Keyword arguments are used in this case as model inputs.
x1  = torch.randn(1, 10) + 5
__output__  = m(**x1)

