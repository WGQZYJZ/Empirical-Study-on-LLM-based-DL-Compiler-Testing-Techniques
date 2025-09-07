
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.dropout(x1, 0.5) # apply dropout to the input tensor
        v2 = torch.rand_like(v) + 13
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
