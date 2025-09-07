
class Model(torch.nn.Module):
    def __init__(self, batchSize):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3, x4):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the first input tensor (x1).
        v2  = torch.mm(v1, x2) 
        v3  = torch.mm(v2, x3) 
        v4  = torch.mm(v3, x4)
        return v4 


# Initializing the model and specifying input tensors for the model
batchSize  = 10 # Batch size
m  = Model(batchSize) 

x1  = torch.randn(batchSize, 8, 64, 64)
__output__  = m(x1, x2, x3, x4)
