
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2 
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model
__input_x1  = torch.randn(80, 50)
__input_x2  = torch.randn(50, 70)
__input_x3  = torch.randn(80, 60)
__input_x4  = torch.randn(60, 90)

__output__  = m(__input_x1,__input_x2,__input_x3,__input_x4)

