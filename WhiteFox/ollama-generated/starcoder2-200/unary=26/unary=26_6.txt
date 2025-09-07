
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask  = v1 > 0
        slope  = negative_slope # Negative slope is 0.2 here.
        neg_mask  = torch.ones(v1.size()).to(v1.device).type(torch.bool) - mask
        result  = neg_mask * slope + mask * v1
        return result


# Initializing the model