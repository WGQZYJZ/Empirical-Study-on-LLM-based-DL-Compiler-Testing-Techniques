
class Model(torch.nn.Module):
    def __init__(self, linear=None):
        super().__init__()
        if linear is not None:
            self.linear = linear

    def forward(self, x1, x2):
        return torch.cat([x1, x2], dim=1)


# Inputs to the model
__inputs__  = (torch.randn(3), torch.randn(4))
m = Model(__inputs__)
