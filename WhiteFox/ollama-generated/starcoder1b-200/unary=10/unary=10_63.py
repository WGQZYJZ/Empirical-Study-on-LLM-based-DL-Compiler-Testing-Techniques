
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8 * 7 * 7, 6)
 
    def forward(self, x):
        v  = self.conv(x)
        v = v.view(-1, 8, 7, 7).contiguous().view(-1, 320)
        v = self.linear(v)
        return torch.clamp_min(v + 3, 0) / 6


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
__output__  = m(x)


