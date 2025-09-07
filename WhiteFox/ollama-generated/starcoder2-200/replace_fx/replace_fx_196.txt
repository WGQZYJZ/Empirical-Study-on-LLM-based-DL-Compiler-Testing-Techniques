
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.3) # Drop out with probability 0.5
        v2 = torch.rand_like(v1) # Generate a 4D tensor filled with random numbers
        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3)
__output__  = m(x1)