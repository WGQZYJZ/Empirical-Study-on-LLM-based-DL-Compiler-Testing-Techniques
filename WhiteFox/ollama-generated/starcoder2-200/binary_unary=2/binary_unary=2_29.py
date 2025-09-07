
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1): 
        v1  = self.conv(x1)
        v2  = v1 - other # subtract another tensor or scalar from the output of the convolution
        v4  = v2 + torch.rand_like(v1) * 0.7071067811865476
        return 0

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3,1231131,1)


