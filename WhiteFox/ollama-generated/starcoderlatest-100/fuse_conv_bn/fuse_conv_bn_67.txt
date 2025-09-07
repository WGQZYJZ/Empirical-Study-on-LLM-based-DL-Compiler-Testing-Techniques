
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, kernel_size=3)

    def forward(self, x):
        conv = self.conv(x)
        bn = F.batch_norm(input=conv)
        return bn

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
