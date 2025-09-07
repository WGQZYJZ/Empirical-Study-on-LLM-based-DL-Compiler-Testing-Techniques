
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1) #v1  = conv_transpose(x1) # Apply the transposed convolution to the input tensor
        v2  = torch.sigmoid(v1)#v2  = torch.sigmoid(t1)  # Apply the sigmoid function to the output of the transposed convolution
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

