
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)

    def forward(self, x1):
        v0 = torch.tanh(x1)
        return self.convt(v0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, 8, 64, 64)
