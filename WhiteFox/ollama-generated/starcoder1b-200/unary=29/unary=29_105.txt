
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 3, 4, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v3 - torch.clamp_min(v2, min_value=-1) + torch.clamp_max(v1, max_value=1)


# Initializing the model
m = Model()

