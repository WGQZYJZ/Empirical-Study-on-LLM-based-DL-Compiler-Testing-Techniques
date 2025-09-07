
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)

        return v3


# Initializing the model and passing it with inputs
m2  = Model2()
__output__  = m2(x1)


