
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v3 = v1 * 0.5 + v2
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v3 * v5
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
