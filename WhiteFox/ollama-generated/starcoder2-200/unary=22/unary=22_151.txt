
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
__input__  = torch.randn(64, 32)
 
# The output of the model on its input __input__ should be:
__output__  = m(__input__)

