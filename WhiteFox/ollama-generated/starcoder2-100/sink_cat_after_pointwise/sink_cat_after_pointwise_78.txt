
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        return torch.cat([x1, x2], 0) \
                .view(-1, x1.shape[-2] * x1.shape[-1])


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 5)
x2 = torch.randn(4, 6)
__output__  = m(x1, x2)