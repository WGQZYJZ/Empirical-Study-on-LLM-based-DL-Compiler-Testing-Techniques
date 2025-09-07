
class Model2(torch.nn.Module):
    def __init__(self, t1 = None):
        super().__init__()

        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        
        if t1 is not None:
            self.other_param  = nn.Parameter(t1, requires_grad=True)
        else:
            self.other_param  = None
        
    def forward(self, x):

        v1   = self.conv(x)
        if self.other_param is not None:
           v2   = v1 - other 
        else:
            v2    = 0
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

