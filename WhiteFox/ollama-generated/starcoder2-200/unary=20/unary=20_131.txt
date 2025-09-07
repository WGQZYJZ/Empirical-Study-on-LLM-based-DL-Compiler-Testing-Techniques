
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._convtranspose2d(x1)
        v3 = torch.sigmoid(v1)
        return v3

    def _convtranspose2d(self,  x):
    	return F.interpolate(x1, scale_factor=0.5, mode='nearest')


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(1, 8, 32, 64)
__output__  = m(x1)

