
class Model(nn.Module):
    def __init__(self, negative_slope=1):
        super().__init__()
        self.conv = nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        mask = (x > 0).type(torch.FloatTensor)
        negative_slope = torch.tensor([self.negative_slope], device='cuda') * mask
        return (self.conv(x).view(-1) * negative_slope).view(mask.shape + (-1))


# Initializing the model
m = Model()


