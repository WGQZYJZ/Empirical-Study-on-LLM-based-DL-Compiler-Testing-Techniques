
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(input1, x1)
        v2  = torch.cat([v1], dim=0) # Concatenate along the first dimension by default
        return v2


# Initializing the model
m  = Model()
 
__inputs_x1__  =  torch.randn(3, 4, 5, 6)  
__inputs_x2__  =  torch.randn(7, 8, 9)
x1  = __inputs_x1__
input1  = x1
 
__inputs_x2__  =  torch.randn(3, 4, 5)  
__inputs_x2__ = __inputs_x2__
x2  = __inputs_x2__
input2  = x2

 # Inputs to the model
x1 = input1
x2 = input2
 
 