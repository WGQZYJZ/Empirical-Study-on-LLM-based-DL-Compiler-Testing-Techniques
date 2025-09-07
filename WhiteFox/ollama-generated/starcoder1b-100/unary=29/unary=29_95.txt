
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=1)
 
    def forward(self, x1, min_value=0, max_value=5):
        v1 = self.conv_transpose(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
