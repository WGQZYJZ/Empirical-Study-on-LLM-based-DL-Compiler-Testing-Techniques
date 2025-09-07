
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1):
        t2 = torch.split(x1, [1], 0)[0] 
        t3 = torch.cat([t2 for i in range(5)], 1)
        return t3

# Initializing the model with input tensor size `(64, 8)`
m = Model(dim=0).cuda()
x1 = torch.randn((64, 8)).cuda()

