
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(4, 8, 4, stride=2, padding=0)

    def forward(self, x1, x2):
        # Add a third input, so the model can distinguish which version of the function was called during training.
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 4, 64, 64)
