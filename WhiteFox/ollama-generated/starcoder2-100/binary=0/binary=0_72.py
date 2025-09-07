
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs): # Here the `other` argument is passed as a keyword argument to the addition operation. 
        v1  = self.conv(x1)
        v2 = v1 + kwargs['other']# Apply the addition operation with other
        return v2

# Initializing the model
m = Model()

# Inputs to the model and keyword argument for `other` tensor passed as a keyword argument of `+`
x1  = torch.randn(1, 3, 64, 64)
kwarg_dict = dict({'other':torch.ones((1,8,1,2))})

