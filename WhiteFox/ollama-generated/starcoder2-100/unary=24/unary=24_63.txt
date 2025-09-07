
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v4  = negative_slope * (v1 - torch.zeros(v1.shape))
        v3  = torch.where(v2, v1, v4) # where(mask, value if mask==True, value otherwise)
        return v3

# Initializing the model with negative slope of 0.25
m  = Model(.25)

