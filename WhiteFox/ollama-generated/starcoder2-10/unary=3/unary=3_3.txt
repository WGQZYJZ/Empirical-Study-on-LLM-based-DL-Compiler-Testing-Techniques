
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0 = torch.randn(4, 5) # Generate input tensor
        v1  = self.conv(v0) 
        v2  = v1 + 1
        return v2


# Initializing the model
m = Model()


# Inputs to the model