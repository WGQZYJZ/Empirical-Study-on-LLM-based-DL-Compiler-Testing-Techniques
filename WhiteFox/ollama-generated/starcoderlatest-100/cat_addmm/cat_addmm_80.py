
class Model(torch.nn.Module):
    def __init__(self, nChannels1, nChannels2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(nChannels1, nChannels2, 3, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, 0) # Perform a matrix multiplication of the two tensors and add it to the input
        v2 = torch.cat([v1], dim=1) # Concatenate along channel dimension and return the result tensor
        return v2


# Initializing the model
m = Model(3, 8)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
