
class Model(torch.nn.Module):
    def __init__(self, dilation_factor):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) 
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) 
        self.dilation_factor = dilation_factor
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return torch.cat([v2 for _ in range(self.dilation_factor)])


# Initializing the model
m = Model(3) 

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
