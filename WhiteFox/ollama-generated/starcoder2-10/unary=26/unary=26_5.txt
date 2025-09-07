
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, kernel_size=7)
        self.leakyrelu = torch.nn.LeakyReLU(negative_slope)
 
    def forward(self, x1):
        v1  = self.convt(x1) # Apply transposed convolution to the input tensor
        v2 = v1 > 0 # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3  = v1 * negative_slope # Multiply the output of the transposed convolution by the negative slope
        v4  = torch.where(v2, v1, v3) # Apply the where function to select elements from t1 or t3 based on the mask v2
        return self.leakyrelu(v4)

# Initializing the model
m  = Model()

