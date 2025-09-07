
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)

    def forward(self, x1, **kwargs):
        return self.conv(x1, **kwargs)

# Initializing the model
m = Model()

