
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Applying a convolution to the input tensor 'inp'
        v2 = torch.mm(v1, v1) + inp 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1,3,64,64)
__inp__ = torch.randn(50,100) # The tensor is randomly generated; you can also specify a concrete tensor here if you want 

#