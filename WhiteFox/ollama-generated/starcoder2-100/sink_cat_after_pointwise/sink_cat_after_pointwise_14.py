
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3 = torch.cat([x1, x2], 0) # concatenating 2 tensors along dimension 0
        return v3[:, :, None]


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5, 8, 4)
x2  = torch.randn(9, 7, 6)
__output__  = m(x1, x2)

# Parameters of the model
m.parameters()

