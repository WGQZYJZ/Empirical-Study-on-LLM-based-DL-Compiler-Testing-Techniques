
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 5 # Add 5 to the result of applying pointwise convolution with kernel size 1 to input_tensor 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # Passing a dummy 5D tensor of shape [1 x 3 x 64 x 64]


__output__= m(x1)

