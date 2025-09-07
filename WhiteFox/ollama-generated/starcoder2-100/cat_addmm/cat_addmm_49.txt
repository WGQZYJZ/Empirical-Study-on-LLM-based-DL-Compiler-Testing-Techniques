
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.mat1 = mat1
        self.mat2 = mat2
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply convolution with stride and pad 0 to the input tensor
        v2 = torch.addmm(v1, self.mat1, self.mat2) # Perform a matrix multiplication of two matrices 
        v3 = torch.cat([v2], dim=0) # Concatenate along dimension 0 after adding v2 to v1
        return v3


# Initializing the model with specific parameters