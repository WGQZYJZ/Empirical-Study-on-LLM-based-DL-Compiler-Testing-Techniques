
class Model(torch.nn.Module):
    def __init__(self, min_value=1.2479666666666667, max_value=5.524460539583817):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model
m = Model(min_value=-0.9590047592091698, max_value=-0.7365222666275404)


