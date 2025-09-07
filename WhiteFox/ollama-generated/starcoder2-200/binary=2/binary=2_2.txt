
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - 5
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

 # The 'other' is a tensor of the same shape as x1
other_tensor  = torch.zeros(size=list(x1.shape))
# or it can be scalar: other = 5 


__output__  = m(x1)


