
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.rand_like(x1)  # Generates a tensor with the same size as input filled with random numbers
        return torch.nn.functional.dropout(v, 0.25)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 3)

__output__  = m(x1)
