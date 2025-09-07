
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.w1, padding=1) # This will fuse the conv and bn into a single conv layer
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 5, 7)
