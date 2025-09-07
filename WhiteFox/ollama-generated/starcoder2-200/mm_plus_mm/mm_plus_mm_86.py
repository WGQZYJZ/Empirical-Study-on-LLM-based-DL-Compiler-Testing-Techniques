
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.mm(x1, y2) 
        return v1

 # Initializing the model
m  = Model()
 
# Inputs to the model
input3  = torch.randn((5,7))
input4  = torch.randn((7,9))
input1  = torch.randn((8, 5))
input2  = torch.randn((8, 7))
__output__  = m(input1, input2)

