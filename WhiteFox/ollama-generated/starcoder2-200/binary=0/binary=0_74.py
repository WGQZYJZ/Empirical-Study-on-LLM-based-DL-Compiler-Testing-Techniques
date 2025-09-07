
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if not isinstance(other, torch.Tensor):
            self.other  = torch.randn(3).detach()
        else: 
            self.other  = other

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.other # Pass keyword argument 'other' to add operation
        return v2


# Initializing the model
m  = Model(None)

