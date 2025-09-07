
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v1  = self.conv3x3(x1)
        v2  = relu(v1)
        return v2
 
 
def conv3x3(in_planes, out_planes, stride=1):
    