
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = self.conv2(x1) # Apply pointwise convolution with kernel size 3 to the input tensor (input 4)
        v1  = torch.abs(v0 - 5.) # Apply the absolute value function to the output of the convolution
        return v1


# Initializing the model