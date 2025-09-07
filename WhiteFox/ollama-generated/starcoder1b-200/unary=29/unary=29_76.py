
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)

    def forward(self, x1, min_value=-20, max_value=20):
        v1 = self.conv(x1, min_value=min_value, max_value=max_value)
        return v1


# Initializing the model
m  = Model()


