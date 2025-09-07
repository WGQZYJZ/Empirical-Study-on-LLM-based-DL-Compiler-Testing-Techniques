
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv1  = torch.nn.ConvTranspose2d(3,8,4)
 
    def forward(self, x1):
        v1  = self.conv1(x1) # Apply a pointwise transposed convolution to the input tensor
        mask  = v1 >0 
        masked_v1  =  torch.where(mask,v1,v1 * negative_slope )# Apply a where function based on whether each element in the output of the transposed convolution is greater than zero or not and then multiply the resulting value by the negative slope
        return masked_v1


# Initializing the model with a negative_slope parameter. 
model = Model(negative_slope=0.2)

# Inputs to the model
inputs  = torch.randn(3,4,64,64)# 4D tensor containing 3 random numbers each representing the 3 channels of an image with width and height as 64x64 


__output__  =model(inputs)
