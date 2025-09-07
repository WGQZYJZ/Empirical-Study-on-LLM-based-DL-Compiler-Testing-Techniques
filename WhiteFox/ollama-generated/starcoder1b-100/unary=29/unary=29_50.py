
class Model(torch.nn.Module):
    def __init__(self, max_value=100, min_value=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        clamped_min_value  = kwargs['clamp_to_zero'] if 'clamp_to_zero' in kwargs else False
        v2 = torch.clamp_min(v1, min_value) if clamped_min_value else v1
        clamped_max_value  = kwargs['clamp_to_one'] if 'clamp_to_one' in kwargs else False
        v3 = torch.clamp_max(v2, max_value) if clamped_max_value else v2
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
