
class Model2(torch.nn.Module):
    def __init__(self, v1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.v1 = v1
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - self.v1 # Subtract 'other' from the output of the convolution
        return v2


# Initializing the model
v0  = torch.zeros([3], device='cuda') 
v4  = torch.ones([8, 3, 64, 64]).float().cuda()
m1   = Model(v0)
 
# Inputs to the model
x2 = v4 # x5 is a tensor of the same shape as 'v4' that has been casted from a float tensor.

 