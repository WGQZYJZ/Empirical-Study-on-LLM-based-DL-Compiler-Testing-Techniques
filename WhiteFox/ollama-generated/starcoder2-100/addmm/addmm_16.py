
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, inp):
        v = torch.mm(input1, input2) + inp
        return v
    
# Initializing the model
m  = Model()

 # Inputs to the model 
 x1 = torch.randn(32, 50).cuda()
 __inp__ = 6
 
 