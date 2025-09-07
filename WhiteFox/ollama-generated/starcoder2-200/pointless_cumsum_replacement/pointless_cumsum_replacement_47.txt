
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer  = torch.nn.Linear(5, 3)
 
    def forward(self, x1): 
        v2  = self.layer(x1) # Apply a linear layer to the input tensor
        return v2
# Initializing the model
m = Model()


# Inputs to the model
__input__ = torch.randn(5) 
__output__  = m(__input__)


