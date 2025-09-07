
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp=None):
        v1 = torch.mm(inp, inp) + inp
        return v1

# Initializing the model
m = Model()
# Inputs to the model
__input1__ = torch.randn(4, 256, 64, 64) # 4 input tensor
__input2__ = torch.randn(32, 64, 128, 128) # 32 input tensor
x = m(__input1__, __input2__)

