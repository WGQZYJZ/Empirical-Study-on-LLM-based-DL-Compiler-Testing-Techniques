
class Model2(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 15)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # ADD HERE
        return v2

m2 = Model2(other=torch.randn(48))

