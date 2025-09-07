

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        splitted  = torch.split(x1, [8], dim=0) 
        concatenated = torch.cat([splitted[i] for i in range(2)], dim=0)
        return concatenated

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(4, 3, 64, 64)
 
 # Output from the model with shape [2, 3, 8]
