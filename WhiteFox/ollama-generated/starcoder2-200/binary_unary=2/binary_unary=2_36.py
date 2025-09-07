
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = torch.randn(500)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 - self.other # The input tensor of subtracting is self.other
        v3  += max((v2), 0) 
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # Input tensor to the model
