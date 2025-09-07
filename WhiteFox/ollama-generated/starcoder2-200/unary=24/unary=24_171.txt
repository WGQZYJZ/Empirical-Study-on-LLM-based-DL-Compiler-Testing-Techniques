
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # apply pointwise convolution with kernel size 1 to the input tensor
        m = (v1 > 0).to_sparse() 
        mask  = torch.full((m.shape), negative_slope, dtype=torch.float32) 
        
        v4  = m * mask + v1
        return v4

m = Model()

