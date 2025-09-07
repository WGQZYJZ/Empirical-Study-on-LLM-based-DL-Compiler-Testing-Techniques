
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = linear(v1)
        v5  = torch.where(torch.gt(v4, 0), v4, negative_slope * v4) # Leaky ReLU
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model 
 x1  = torch.randn(1,3,64,64)
 
