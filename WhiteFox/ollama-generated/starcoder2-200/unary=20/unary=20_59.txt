
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        convtranspose  = torch.nn.ConvTranspose2d(32, 8, (5, 4), stride=(3, 6))
        v2 = self._apply_sigmoid(convtranspose) # Applying the sigmoid function to the transposed convolution output
        return v2
        
    def _apply_sigmoid(self, module):
        for p in module.parameters():
            p *= torch.rand_like(p) + 0.5
        return module


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(8, 32, 496, 728)
