
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(1, 3)
        v1 = self.linear(v0)
        v2 = v1 - other 
        return v2
