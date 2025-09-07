
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1) # Pointwise transposed convolution
        self.negative_slope = negative_slope # Assigning a negative slope
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.convt(x1)
        mask = (v1 > 0).float().detach() # Applying the mask to each element in v1
        v2  = v1 * (-self.negative_slope)
        v3  = torch.where(mask, v1, v2) 
        return self.relu(v3)

# Initializing the model with a negative slope of -0.5
m = Model(-0.5)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # Input tensor
