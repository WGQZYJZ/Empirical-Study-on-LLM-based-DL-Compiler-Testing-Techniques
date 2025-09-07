
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.empty((3, 8)) 
        v4 = v2 + other
        v5 = torch.relu(v4)  
        return v5


# Initializing the model
m  = Model()
other = m.__output__
 
 # Inputs to the model 
 x1 = torch.randn(1, 3, 64, 64)
 __output__  = m(x1)
 
 
