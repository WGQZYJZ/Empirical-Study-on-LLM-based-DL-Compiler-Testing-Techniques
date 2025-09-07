
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
        self.conv.weight  = negative_slope
        self.conv.bias  = -negative_slope
 
    def forward(self, x1): 
        v1  = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        mask   = torch.gt(v1, 0).float()  # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2  = v1 * self.conv.weight  # Multiply the output of the transposed convolution by the negative slope 
        v3  = torch.where(mask, v1, v2) # Apply the where function to select elements from v1 or v2 based on the mask mask
        return v3


# Initializing and running the model with `negative_slope` set to 0.5
negative_slope   = 0.5
m                = Model(negative_slope).cuda()
input            = torch.randn(1, 8, 64, 64)
output           = m(input.cuda())

