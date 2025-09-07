
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).flatten().contiguous()
        v2 = (v1 * 0.5).to(dtype=torch.float64, layout='cpu', device=device, pin_memory=False)
        v3 = (v1 * 0.7071067811865476).to(dtype=torch.float64, layout='cpu', device=device, pin_memory=False)
        v4 = torch.erf(v3)
        v5 = (v4 + 1).to(dtype=torch.float64, layout='cpu', device=device, pin_memory=False)
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


