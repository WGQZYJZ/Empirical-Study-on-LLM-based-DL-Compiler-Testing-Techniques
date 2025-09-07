
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
    
    def forward(self, x1):
        v1  = F.max_pool2d(x1, 2) 
        v40  = F.interpolate(v1, scale_factor=2, mode="nearest") 
        return v40

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 8, 64)
__output__  = m(x1)

