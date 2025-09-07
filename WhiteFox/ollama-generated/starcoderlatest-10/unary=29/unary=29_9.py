
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        min_value = torch.tensor(v1.min())
        max_value = torch.tensor(v1.max())
        t2 = torch.clamp_min(v1, min=min_value)
        t3 = torch.clamp_max(t2, max=max_value)
        return t3


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
