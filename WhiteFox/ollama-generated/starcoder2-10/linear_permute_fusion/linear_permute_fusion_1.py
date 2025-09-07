
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor without the permute method.
        v2  = v1.permute(...)
        return v2

# Initializing the model
m  = Model()


# Inputs to the model