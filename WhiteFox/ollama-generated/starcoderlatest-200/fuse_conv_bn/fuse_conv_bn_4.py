 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, 5)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.batch_norm(v1, ...) # Use the output of conv layer as input
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
