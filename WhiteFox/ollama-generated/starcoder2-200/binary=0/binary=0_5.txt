
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
 
    def forward(self, x1):
        t2 = self.conv(x1) + kwargs['other']
        return t2

 # Initializing the model with a new keyword argument
 m  = Model(**{'other': torch.randn(3)})
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 __output__  = m(x1)
 
