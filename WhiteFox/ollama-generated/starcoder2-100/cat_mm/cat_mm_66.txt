
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()
        self.mm = torch.matmul
 
    def forward(self, x1, y2): 
        v1  = mm(x1,y1)
        v2  = cat([v1 for i in range(dim)])
        return v2
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(5,3) 
 y2 = torch.randn(50,3)
 
 __output__  = m(x1,y2)
