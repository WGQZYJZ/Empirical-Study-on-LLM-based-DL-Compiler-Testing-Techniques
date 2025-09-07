
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, kernel_size=(1, 5))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.batch_norm(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 1, 5)
