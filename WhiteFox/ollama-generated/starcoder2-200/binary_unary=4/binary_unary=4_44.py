
class Model(torch.nn.Module):
    def __init__(self, other: Tensor = torch.randn((10,))):
        super().__init__()
 
    def forward(self, x2):
        v3  = self.conv1(x2) + other 
        return v4


# Initializing the model
m  = Model()

# Inputs to the model 
x2 = torch.randn(1, 100, 64, 64)
