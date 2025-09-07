
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=0)
        v3  = v1.view(-1, 5).tanh()
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 6)
x2 = torch.randn(7, 8)
__output__  = m(x1, x2)
