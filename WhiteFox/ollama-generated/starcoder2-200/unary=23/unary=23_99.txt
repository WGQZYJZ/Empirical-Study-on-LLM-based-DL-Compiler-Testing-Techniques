
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.convt  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.convt(x1) 
        v2  = torch.tanh(v1)  
        return v2


# Initializing the model:
m = Model()
__output__  = m(torch.randn(4,8,64,64))

The size of the output tensor can be (4,3,64,64), which is consistent with the shape of input tensor and its transposed convolution.

