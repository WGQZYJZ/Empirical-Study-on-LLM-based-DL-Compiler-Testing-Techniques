
class Model(nn.Module):
    def __init__(self, negative_slope: float):
        super().__init__()
        self.conv  = nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = F.leaky_relu(self.conv(x1))
        # Add a transpose convolution to the input tensor
        v2 = v1 * torch.exp(- self.negative_slope * torch.abs(v1))
        return v2


# Initializing the model
m  = Model(1)


