
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1):
            return torch.split(x1, [64], 0)

 # Initializing the model and obtaining the output using a dummy input tensor:
m = Model()
__output__  = m(torch.randn(32, 784))
 
 