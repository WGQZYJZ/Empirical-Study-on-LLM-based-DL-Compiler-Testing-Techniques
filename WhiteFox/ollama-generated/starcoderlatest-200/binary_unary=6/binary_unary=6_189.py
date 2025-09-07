
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8, bias=True)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v3 = torch.nn.ReLU()(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
