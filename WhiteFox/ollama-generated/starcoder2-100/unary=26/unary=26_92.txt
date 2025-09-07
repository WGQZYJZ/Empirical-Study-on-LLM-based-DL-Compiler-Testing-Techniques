
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,kernel_size=(1,1), stride=1)
        self.linear = torch.nn.Linear(in_features=4*8*96*96, out_features=50)
        self.neg_slope = negative_slope
 
    def forward(self, x):
        v  = self.conv(x).reshape(-1,32 * 9 * 9) # Apply the pointwise transposed convolution to an input tensor
        v2 = (v > 0).type(torch.float) # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise 
        v4 = torch.where(v2 , v , v * self.neg_slope)# Apply the where function to select elements from v or v3 based on the mask v2
        return v

# Initializing the model
m  = Model()
 
# Inputs for the model
x1 = torch.randn((1, 3, 96, 96))
__output__  = m(x)

