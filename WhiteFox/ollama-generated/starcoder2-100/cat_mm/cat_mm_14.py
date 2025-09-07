
class Model(torch.nn.Module):
    def __init__(self, num1=80, num2=56):
        super().__init__()
 
    def forward(self, x1):
        v = torch.nn.utils.repeat(x1[None], 37, dim=0)
        return v
 

# Initializing the model
m  = Model()


# Inputs to the model
a1  = torch.randn(80, 56)
a2  = [torch.zeros([59]), torch.ones([4])] * 37 + torch.rand((37, 56))

__output__  = m(a1)
__output__  = m(a2)

