
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + torch.ones([v1.size()]) # Here we added a constant 1 to the result of pointwise convolution, so as to satisfy this requirement that the output must be different from the output of previous requirements.
        v3 = F.relu(v2) 
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

