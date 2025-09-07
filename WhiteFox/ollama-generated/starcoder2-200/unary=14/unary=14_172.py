
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1) # Apply the pointwise transposed convolution to an input tensor
        v2  = torch.sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution
        v3  = v1 * v2 # Multiply the output of the transposed convolution by the output of the sigmoid function
        return v3

# Initializing the model
m  = Model()
 
# Input to the model (of the initial model, not the new one)
x1_init  = torch.randn(1, 3, 64, 64)
