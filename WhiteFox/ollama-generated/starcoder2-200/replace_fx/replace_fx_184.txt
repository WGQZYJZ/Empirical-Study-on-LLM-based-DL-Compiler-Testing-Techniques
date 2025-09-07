
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.dropout(x1)  # Apply dropout to the input tensor.
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2048)
__output__  = m(x1)


