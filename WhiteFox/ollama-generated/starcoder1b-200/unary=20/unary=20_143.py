
class UpsampleModel(torch.nn.Module):
    def __init__(self, conv_dim):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, conv_dim // 2, 4, stride=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
model = UpsampleModel(8)

