
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        v1 = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + torch.randn_like(v1)# Add another tensor to the output of the convolution
        v3 = torch.relu(v2) 
        return v3

m  = Model()


# Initializing model and inputs 
__output__  = m(torch.randn(1, 3, 64, 64))

__output__  = m(torch.randn(10, 3, 64, 64))

