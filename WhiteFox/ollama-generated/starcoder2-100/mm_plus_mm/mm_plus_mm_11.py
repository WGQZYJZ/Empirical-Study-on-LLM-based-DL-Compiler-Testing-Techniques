
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        t2  = torch.mm(x1, y1)
        return t2
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(4096, 512)
y1  = torch.randn(512, 512)
 
 __output__  = m(x1, y1).sum()
