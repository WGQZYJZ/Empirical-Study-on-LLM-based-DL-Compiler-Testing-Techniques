
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1): 
        v1  = torch.mm(x1, y1)
        v2  = torch.mm(y1, x1)
        return v1 + v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(640,32)
y1  = torch.randn(32,70)

 #__output__  = m(x1, y1)
 
