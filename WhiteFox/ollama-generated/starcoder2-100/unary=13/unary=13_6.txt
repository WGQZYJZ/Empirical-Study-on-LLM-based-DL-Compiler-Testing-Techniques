
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.sigmoid(x3)
        v4  = x4 * v2
        return v4

 # Initializing the model
m = Model()
 
 # Inputs to the model
x50 = torch.randn(768*960-768*16-1, 512).cuda()
