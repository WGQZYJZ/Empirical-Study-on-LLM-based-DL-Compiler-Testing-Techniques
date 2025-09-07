
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=-1e9):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + min_value
        v3  = v2.clamp_(min_value=-90., max_value=-6.)
        return v3
# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 57, 4)
__output__  = m(x1)

# Please provide inputs and expected outputs for all public PyTorch APIs.
