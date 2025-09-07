
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3,8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.convtranspose(x1) # Apply the transposed convolution operation to the input tensor
        v2 = torch.sigmoid(v1) 
        return torch.mul(v2, v1)


# Initializing model and setting random seed for reproducibility.
m  = Model()
torch.manual_seed(4359874)
__output__  = m(x1) # Running the forward pass of the model on input x1

