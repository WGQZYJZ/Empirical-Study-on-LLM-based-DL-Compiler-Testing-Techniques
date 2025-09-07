
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.ops._caffe2.conv_spatial(x1)
        v2  = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3) + 1
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2, 8 , 64, 64)
__output__  = m(x1)

