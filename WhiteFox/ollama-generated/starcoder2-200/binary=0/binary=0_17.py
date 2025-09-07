
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
    
    def forward(self, x1): 
        v1  = self.conv(x1) # apply the pointwise convolution with kernel size 1 to the input tensor
        return v1 + other
    
m  = Model()
        
# Inputs to the model
other = torch.zeros_like(x1)
x1  = torch.randn(1,3,64,64)

