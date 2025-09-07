
class Model(torch.nn.Module):
    def __init__(self, t1=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        v2 = v1 + kwargs['t1'] # add to the output of the convolution a tensor that is passed in as a keyword argument
        return v2


# Initializing the model 
m = Model()

# Input tensors for the model
t1  = torch.randn(1, 3, 64, 64) # This is an input to the model because we pass it in as a keyword argument
__output__  = m(x1=t1, t1=0.2*t1)

