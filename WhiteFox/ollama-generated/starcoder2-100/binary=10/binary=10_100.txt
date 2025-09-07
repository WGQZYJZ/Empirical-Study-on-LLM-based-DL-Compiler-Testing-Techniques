
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        return v1 + other
        
  # Initializing the model        
m  = Model()

# Input to the model          
other  = torch.randn(4096)
x1  = torch.randn(5, 32, 7, 7)
__output__  = m(x1)
