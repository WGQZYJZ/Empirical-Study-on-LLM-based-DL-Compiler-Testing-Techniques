
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        clamped_output = torch.clamp(v1, min=self.min_value, max=self.max_value)
        return clamped_output


# Initializing the model
m = Model(min_value=-3, max_value=3)
__output__  = m(x1)


