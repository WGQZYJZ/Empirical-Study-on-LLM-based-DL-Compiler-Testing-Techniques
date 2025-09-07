
class Model(nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = nn.ConvTranspose2d(3, 8, kernel_size=(1, 4), stride=2, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = F.leaky_relu(self.conv(x1))
        v2 = torch.where(v1 > 0, v1 * self.negative_slope, 0)
        return v2


# Initializing the model
m = Model()


