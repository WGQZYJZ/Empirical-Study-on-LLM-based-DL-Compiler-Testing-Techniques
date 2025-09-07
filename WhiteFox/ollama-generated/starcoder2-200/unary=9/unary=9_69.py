
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # add 3 to output of convolution
        v3  = torch.clamp_min(v2,0) # clamp the output after addition by minimum value 0
        v4  = torch.clamp_max(v3,6) # clamp maximum 6
        v5  = v4 / 6 # devide by 6 for normalization
        return v5
# Initializing model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


