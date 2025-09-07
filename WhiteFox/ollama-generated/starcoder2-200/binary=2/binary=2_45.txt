
class Model(torch.nn.Module):
    def __init__(self, constant=1):
        super().__init__()
        self.constant = constant  # Other value
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2


# Initializing the model with different values for other variable in forward call of __call__ function
m  = Model(constant=0.)
other  = torch.tensor([1], device='cuda') # Other value

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

