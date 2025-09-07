
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
        self.leakyrelu = nn.LeakyReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1) # Transposed convolution operation
        v2 = (v1 > 0).type_as(v1) # Create a mask where each element is True if the corresponding value in t1 is greater than 0, False otherwise 
        v3 = negative_slope * v1 # Multipy the output of the transposed convolution by the negative slope
        v4 = torch.where(v2 == True, v1, v3) # Apply the where function to select elements from v1 or v3 based on the mask v2
        return self.leakyrelu(v4)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
