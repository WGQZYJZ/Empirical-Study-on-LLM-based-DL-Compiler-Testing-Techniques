
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.act = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v6  = self.act(v1)
        return v6


# Initializing the model
m2  = Model2()

# Inputs to the model
x1  = torch.randn(48, 32, 500, 768)
__output_2__  = m2(x1)


