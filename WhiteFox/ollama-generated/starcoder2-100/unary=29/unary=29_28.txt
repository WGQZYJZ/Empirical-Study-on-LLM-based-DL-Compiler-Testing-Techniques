
class Model(torch.nn.Module):
    def __init__(self, minval=-30.942856713753878, maxval=33.94373200307628):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.deconv(x1)

        return


# Initializing the model and setting minval & maxval to values
m = Model(-30.942856713753878, 33.94373200307628)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

