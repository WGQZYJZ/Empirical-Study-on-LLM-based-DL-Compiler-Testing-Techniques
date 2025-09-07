
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 10, kernel_size=5)

    def forward(self, x):
        return F.batch_norm(F.conv2d(x, self.conv))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
