
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inputs):
        return torch.cat([inputs[:,0:2], inputs[:,2:]], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(3, 64, 64)
__output__  = m(x)

