
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *inputs):
        v0 = torch.cat(list(*inputs), dim=1)
        v1 = v0[:, 9223372036854775807]

        return v1

# Initializing the model
m = Model()

# Inputs to the model
x0 = torch.randn(1, 3, 64, 64) # Shape of x0 is [1, 3, 64, 64]. It is a dummy input.
x1 = torch.randn(25, 3, 8)  # Shape of x1 is [25, 3, 8]
__output__  = m([x0, x1])

