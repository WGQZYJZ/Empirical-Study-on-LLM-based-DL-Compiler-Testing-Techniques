
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) #Apply pointwise transposed convolution to the input tensor
        v2  = torch.sigmoid(v1)# Apply sigmoid function to output of transposed convolution
        v3  = v1 * v2# Multiply the output of transposed convolution by the output of sigmoid function
__output__  = m(x1)

