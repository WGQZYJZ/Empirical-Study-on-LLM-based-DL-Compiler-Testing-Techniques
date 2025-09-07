
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        msk = v1 > 0  # Select elements greater than zero from the output of the convolution
        v2  = torch.relu(v1, inplace=False)  # Create a copy of the input to the ReLU function that is non-destructive
        v3  = -2 * v1 
        v4  = v2 * v3
        return x1 * msk + v4


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

