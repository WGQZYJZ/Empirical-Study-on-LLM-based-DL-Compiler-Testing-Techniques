
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.full([v1], 1, dtype=torch.float32, layout=torch.strided, device=x1.device, pin_memory=False) * 0.5
        v3 = torch.full([v1], 1, dtype=torch.float32, layout=torch.strided, device=x1.device, pin_memory=False) * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64, device='cuda')
