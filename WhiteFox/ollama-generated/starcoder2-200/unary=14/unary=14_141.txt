
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1  = self.convt(x1) # Apply the pointwise transposed convolution to the input tensor
        v2  = self.sigmoid(v1) 
        v3  = v1 * v2 # Multiply the output of the transposed convolution by the output of the sigmoid function

        return v3


m = Model()


# Initializing the model