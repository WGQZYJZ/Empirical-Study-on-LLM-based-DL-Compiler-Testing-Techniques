
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.linear  = torch.nn.Linear(64 * 64 , 8*3)
 
    def forward(self, x):
        v1  = self.conv(x) # Apply the pointwise convolution to an input tensor with the kernel size of 1 and stride 1 without padding on each dimension 
        v2  = torch.flatten(v1, start_dim=1)
        v3  = self.linear(v2)
        
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(8, 3, 64 , 64 )
__output__  = m(x)

