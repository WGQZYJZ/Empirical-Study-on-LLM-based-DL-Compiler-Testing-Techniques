
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.3, max_value=1.25):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(
            8, 3, (64), stride=(1,), padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value=-0.3)
        v3  = torch.clamp_max(v2, max_value=1.25)
        return v3


# Initializing the model
m  = Model(-0.3, 1.25)


# Inputs to the model