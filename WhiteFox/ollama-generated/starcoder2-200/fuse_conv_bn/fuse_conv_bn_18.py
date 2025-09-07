
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 4, 3)

        bn = torch.nn.BatchNorm2d(4, affine=False)
        
        v1 = conv(x1)
        v2 = bn(v1)

        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(3, 5, 9)

# Run model and get the output tensor
