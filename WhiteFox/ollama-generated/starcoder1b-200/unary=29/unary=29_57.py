
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return torch.clamp_min(v1, min_value)


# Initializing the model
m = Model()


