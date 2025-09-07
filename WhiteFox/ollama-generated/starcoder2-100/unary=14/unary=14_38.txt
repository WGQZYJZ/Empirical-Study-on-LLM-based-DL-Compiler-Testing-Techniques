
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.convTrans(x1) 
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2 # Apply the sigmoid function to the output of the transposed convolution.
        return v3


# Initializing the model