
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor 
        return v1 + torch.randn(v1.shape)


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
# Input tensor for the new model that is not part of the previous model
other_tensor = torch.randn(100,) # a vector of 100 random numbers with 8 values per each of them (for example, 5.739592 6.444759 5.939594 -0.539587  ...)


# Initializing the new model
new_m = Model()
 
# Inputs to the new model that is not part of the previous model
x1 = torch.randn(2, 3, 64, 64)

