

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1) # <-- The sigmoid activation function is applied to the transposed convolution output here
        return v2


# Initializing the model
m = Model()


# Inputs to the model