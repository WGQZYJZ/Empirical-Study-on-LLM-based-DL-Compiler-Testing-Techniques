
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1, padding=0)
 
    def forward(self,x1,x2):
        v1  = torch.mm(x1, x2) 
        v2  = v1 + inp
        return v2


# Initializing the model and passing 'inp' as a keyword argument to 'forward' function of the model.
m  = Model()
 
#Inputs to the model  
inp  = torch.randn(3, 4) #Tensor with shape (3, 4) 
x1  = torch.randn(128, 50, 64, 64) # Tensor with shape (128, 50, 64, 64). This tensor is passed as input to the 'forward' function of 'Model' and it should be different from its previous one.
x2 = torch.randn(3, 4)
 
m(inp, x1, x2=x2)

