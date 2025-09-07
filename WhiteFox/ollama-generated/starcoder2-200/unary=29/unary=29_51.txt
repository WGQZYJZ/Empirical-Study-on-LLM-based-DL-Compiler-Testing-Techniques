
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.upsample  = torch.nn.Upsample(scale_factor=4, mode="nearest")
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * max_value - min_value 
        return v2

# Initializing the model