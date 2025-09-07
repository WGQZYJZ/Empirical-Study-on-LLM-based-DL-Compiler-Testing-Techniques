
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=256):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3

# Initializing the model and providing minimum and maximum values to clamp between 0 and 256
m = Model(min_value=0, max_value=256)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
