
class Model(torch.nn.Module):
    def __init__(self, input1=32, input2=32):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) 
        v2 = torch.cat([v1] * 50, dim=-1)  
        return v2


# Initializing the model
m  = Model()
 
__output__, __x1__, __x2__  = m(torch.randn(32), torch.randn(32))


