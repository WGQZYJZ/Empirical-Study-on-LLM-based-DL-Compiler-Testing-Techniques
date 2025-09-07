
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
        if other is not None:
            self.other  = torch.nn.Parameter(data=other, requires_grad=False)
 
    def forward(self, x1):
        v1  = self.conv(x1) + self.other 
        return v1

m = Model(other=torch.zeros([3]))

 # Inputs to the model 
 x1 = torch.randn(1, 3, 64, 64)
 __output__  = m(x1)
 
 

