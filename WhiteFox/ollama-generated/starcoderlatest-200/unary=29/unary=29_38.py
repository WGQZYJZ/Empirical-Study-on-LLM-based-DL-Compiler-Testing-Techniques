
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value=None):
        super().__init__()
        if not max_value:
            self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=8, padding=4)
        else:
            self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=8, padding=4)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        if not max_value:
            min_value = torch.finfo().eps
        if min_value:
            v2 = torch.clamp_min(v1, min_value=min_value)
        else:
            v2 = torch.clamp(v1, 0, float('inf'))
        if max_value:
            v3 = torch.clamp_max(v2, max_value=max_value)
        else:
            v3 = torch.clamp(v2, -float('inf'), 0)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
