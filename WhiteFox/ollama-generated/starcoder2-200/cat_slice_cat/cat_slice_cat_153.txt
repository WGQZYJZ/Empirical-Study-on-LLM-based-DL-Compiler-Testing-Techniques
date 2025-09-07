
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.cat([x1], dim=2)
        return [v0]
 
 
# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(45839678725978, 9223372036854775807) # Generate a random 3D tensor with size (45839678725978, 1).
 

