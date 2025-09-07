
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=2.):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=4, stride=2)

    def forward(self, x1, min_value=0.1, max_value=2.):
        v1 = self.conv(x1)
        v2 = v1.clamp(min_value=min_value).max(min_value=max_value).squeeze()
        return v2


# Initializing the model
m = Model(min_value=-3, max_value=4.)
