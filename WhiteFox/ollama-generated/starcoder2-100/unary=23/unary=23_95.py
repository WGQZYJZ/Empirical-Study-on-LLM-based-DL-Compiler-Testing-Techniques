
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = x1 # Save the original input tensor
        v4_outputsize = v0.size()
        t5  = torch.zeros((v0.size()[0], 796))
        v3  = t5 + v0
        t2  = self.convt(v3)
        v1  = t2 # Save the output of the transposed convolution
        v4  = torch.tanh(v1)
        return v4, v4_outputsize


# Initializing the model
m = Model()

# Inputs to the model