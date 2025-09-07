
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
    
    def forward(self, x1): 
        v1 = self.conv_transpose(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.sigmoid(v1) # Apply sigmoid function to the output of the transposed convolution
        v3 = v1 * v2  # Multiply the output of the transposed convolution by the output of the sigmoid function
        return v3

# Initializing the model
m  = Model()

