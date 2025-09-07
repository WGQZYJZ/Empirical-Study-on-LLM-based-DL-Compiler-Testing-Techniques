
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.randn(3, 4).to("cuda")
        v1 = self.linear_(v0)
        return v1

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.randn(3, 4).to("cuda")
        v1 = self.linear_(v0)
        return v1

