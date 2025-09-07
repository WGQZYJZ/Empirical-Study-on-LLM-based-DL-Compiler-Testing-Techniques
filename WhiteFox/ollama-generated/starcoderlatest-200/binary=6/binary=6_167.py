
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 16)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model2()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.tensor([0.5])
