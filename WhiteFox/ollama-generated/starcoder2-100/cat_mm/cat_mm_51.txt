
class Model(torch.nn.Module):
    def __init__(self, ksize=3):
        super().__init__()
        self.ksize = ksize
        self.conv  = torch.nn.Conv2d(16 * self.ksize ** 4, 8 * self.ksize ** 5, self.ksize)

    def forward(self, x0):
        v0_0  = [torch.mm(v0[i], v0[- (i + 1)]) for i in range(len(x))] # Matrix multiplication of two input tensors
        v2_0  = torch.cat([x[:,:,:, 8] * x[:-9,:,:,:] for x in x]) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(32, 4, 64)
x2  = torch.randn(32, 80, 75)
__output__  = m(x1)

