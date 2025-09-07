
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv3d(x1, 3) # Input is a 5D input tensor with size (N x C x D x W x H) 
        v2 = torch.nn.functional.batch_norm(v1, momentum=0.9)
        return v2

# Initializing the model
m  = Model()
x1 = torch.rand(3, 4, 5, 6, 7).cuda()
# Fusing Conv3d and BatchNorm2d
__output__  = m(x1)

