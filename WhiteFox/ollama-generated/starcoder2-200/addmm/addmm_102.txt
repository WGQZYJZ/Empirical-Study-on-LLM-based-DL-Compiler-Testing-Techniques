
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp 
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
inp  = torch.randn(64, 3072)
x1  = torch.randn(59, 85).type(torch.FloatTensor), 
x2  = torch.randn(59*3072, 85*85).type(torch.FloatTensor)
 
# Initializing the model with custom input tensor
x1  = torch.randn(64, 3072)
m1  = Model().cuda() # On GPU device (for example, GPU id=0 or GPU id=1 )
__output__  = m1(x1)
 
