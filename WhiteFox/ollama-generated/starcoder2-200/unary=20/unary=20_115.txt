
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv_t = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v0  = self.conv_t(x1) # Apply pointwise transposed convolution to the input tensor
        
        v1  = torch.sigmoid(v0) 
        return v1
# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(2,3,64,64) 
 __output__  = m(x1)
