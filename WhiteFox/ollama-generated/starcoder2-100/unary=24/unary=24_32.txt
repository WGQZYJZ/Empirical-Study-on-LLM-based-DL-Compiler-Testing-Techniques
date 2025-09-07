
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1591):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)

    def forward(self, x):
       v1 = self.conv(x) 
       v2 = v1 > 0
       v3 = negative_slope * (v1 - 0) 
       v4 = torch.where(v2, v1, v3)

       return v4

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

