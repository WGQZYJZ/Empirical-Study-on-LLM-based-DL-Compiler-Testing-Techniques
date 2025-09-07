
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return linear(x1) + other
 
 # Initializing the model
 m  = Model()
 
 # Inputs to the model
 x1  = torch.randn(5, 2048)
 
# Output of the model (for checking)
__output__  = m(x1)