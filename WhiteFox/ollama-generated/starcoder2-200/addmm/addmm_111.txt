

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        return v1 + inp
    


# Initializing the model
m  = Model()

 # Inputs to the model
 
__input_tensor1__, __input_tensor2__ = torch.randn(480), torch.randn(479)

 
# Outputs of the model:
__output__  = m(__input_tensor1__, __input_tensor2__)


