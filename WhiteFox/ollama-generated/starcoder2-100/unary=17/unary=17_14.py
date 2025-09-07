
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1 = conv_transpose(x1) 
        v2 = relu(v1)
        return v2


# Initializing the model and inputs to the model
m = Model()
x1 = torch.randn(10, 8, 64, 64) # Input tensor size: 32 x 3 x 64 x 64
