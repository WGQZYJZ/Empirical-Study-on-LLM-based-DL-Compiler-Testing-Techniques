
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.rand_like(x1).dropout(p=0.5)  # apply dropout on the permuted tensor
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)

# Running the model:
__output__  = m(x1)

