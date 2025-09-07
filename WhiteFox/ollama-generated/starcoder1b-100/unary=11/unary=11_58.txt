
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) + 3
        return torch.clamp_min(v1, 0), torch.clamp_max(v1, 6) / 6


# Initializing the model
m = Model()


