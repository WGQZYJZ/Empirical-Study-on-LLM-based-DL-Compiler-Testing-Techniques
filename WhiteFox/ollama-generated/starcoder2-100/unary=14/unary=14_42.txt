
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution
        v3  = v1 * v2  # Multiply the output of the transposed convolution by the output of the sigmoid function 
        return v3


# Initializing the model and the output of the initial model is generated
m  = Model()
output_m0 = m(x1) 

