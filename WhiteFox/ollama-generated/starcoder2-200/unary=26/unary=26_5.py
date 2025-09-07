
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.5):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
      v1 = self.convtranspose(x1) # Apply pointwise transposed convolution to the input tensor
      mask  = v1 > 0 
      v2 = torch.where(mask,v1,-negative_slope*v1 )# Apply the where function to select elements from v1 or negative_slope*v1 based on the mask
      return v2

# Initializing the model and setting the slope parameter
m = Model()
negative_slope  = torch.Tensor([0.5])

 # Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)
