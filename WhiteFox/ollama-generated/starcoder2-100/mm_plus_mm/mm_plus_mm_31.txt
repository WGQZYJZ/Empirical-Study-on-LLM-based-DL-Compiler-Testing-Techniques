
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2):
        v1  = torch.mm(x1,y1)
        v2  = torch.mm(x2,y2)
        v3  = v1 + v2 
        return v3
 
# Initializing the model
m  = Model()

 # Inputs to the model 
x1  = torch.randn(4096, 576)  
x2  = torch.randn(576, 832)
y1  = torch.randn(4096)    
y2  = torch.randn(832)
__output__  = m(x1, y1, x2, y2)

