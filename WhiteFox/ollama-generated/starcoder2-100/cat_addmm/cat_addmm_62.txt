
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.cat = torch.nn.Cat()
 
    def forward(self, x):
         v0  = torch.randn(5,64).cuda()
         v1 = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
         v2 = v0 + v1 
         v3 = v2.mul_(v2) 
         v4 = v0 + torch.rand((5,)).mul(1.) 
         v5 = v4 + torch.randn_like(v4).cuda().mul(-torch.rand()) # Multiply the output of the error function by a random scalar
         v6 = self.cat([v3], dim) 
        return  (v0,)

# Initializing the model with custom dim input tensor 
m1 = Model(dim=5).cuda()


# Inputs to the model from the previous example:
input_tensor,  x  =  torch.randn((64,3)).cuda(), torch.randn(size=(64,80,32,32), dtype=torch.float)
__output__  = m1(*[x])
