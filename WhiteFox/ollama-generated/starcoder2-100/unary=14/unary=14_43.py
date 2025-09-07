
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = self.convT(x) # Applying the transposed convolution to an input tensor. 
        v2  = torch.sigmoid(v1) # Applying a sigmoid function to the output of the convolution
        v3  = v1 * v2 # Multiplying the output of the transposed convolution by the output of the sigmoid function
        
        return v3


m = Model()



# Initializing the model with 1024, 8 channels, 64 x 64 input.
m(torch.randn(1024, 8, 64, 64))

