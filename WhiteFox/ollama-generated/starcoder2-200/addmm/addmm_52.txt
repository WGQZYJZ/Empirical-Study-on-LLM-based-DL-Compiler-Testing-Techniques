
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = torch.mm(x1, x2)
        if  'inp' in self.__dict__:
            v2 = inp + v1
        else:
             inp  = v1
        return v2

# Initializing the model
m = Model()

 # Inputs to the model (Tensor shape is 3 * 5)
x1, x2  = torch.randn(3, 4), torch.randn(5, 6)
__output__  = m(x1, x2)

