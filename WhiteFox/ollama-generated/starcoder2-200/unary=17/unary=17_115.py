
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = conv(x1)
        v2 = relu(v1) # This model contains one pointwise transposed convolution followed by a ReLU activation function
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)
