
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
other = torch.randn(8, 3, 64, 64) # An input tensor that is not used in this model. The model contains a tensor of the same shape but the name is 'other'. 
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

