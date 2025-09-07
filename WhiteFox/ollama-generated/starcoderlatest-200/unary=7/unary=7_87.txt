
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16, bias=True)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = v1 * (torch.clamp((v1 + 0), min=0, max=6))
        v3 = v2 / 6
        return v3
