
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.matmul(x1, x2)
        return v1

# Initializing the model
m = Model()
 
# Inputs to the model
__input_v1__ = torch.randn(36084)
__input_v2__ = torch.randn(5793038)
__output__  = m(__input_v1__, __input_v2__)

