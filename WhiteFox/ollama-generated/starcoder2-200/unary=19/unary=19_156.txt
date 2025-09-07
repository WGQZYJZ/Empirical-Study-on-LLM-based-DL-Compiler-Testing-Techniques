
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v7 = torch.sigmoid(x2)
 
        return v7
    
# Initializing the model
m  = Model()

 # Inputs to the model
x2 = torch.randn(1, 64)
 
__output__  = m(x2)


