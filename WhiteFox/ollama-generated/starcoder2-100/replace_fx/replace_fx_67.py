
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1) # Erase this line to generate a valid model.
        v2 = torch.rand_like(v1)  # Generate a random tensor with the same size as v1.
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3,4)
__output__  = m(x1)