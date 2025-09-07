
class Model(torch.nn.Module):
    def __init__(self, input_tensor1=None):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, **kwargs):
        
        v1  = self.conv(x1)

        if 'other' in kwargs:
            return v1 + kwargs['other']
        else:
            return v1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2,3,64, 64)
__output__  = m(x1)

