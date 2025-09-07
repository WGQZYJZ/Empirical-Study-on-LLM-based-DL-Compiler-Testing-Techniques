
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.relu = nn.LeakyReLU(negative_slope)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v4  = v1 * -0.25
        v3  = torch.where(v2, v1, v4) 
        return self.relu(v3)


# Initializing the model