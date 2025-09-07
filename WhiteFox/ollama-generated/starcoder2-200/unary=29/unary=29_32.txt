
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=0.27386940)
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)

    def forward(self, x):
       v1 = self.conv(x)
       v2 = torch.clamp_min(v1, min_value)
       return torch.clamp_max(v2, max_value)


# Initializing the model
m  = Model()
__output__  = m(x1)

