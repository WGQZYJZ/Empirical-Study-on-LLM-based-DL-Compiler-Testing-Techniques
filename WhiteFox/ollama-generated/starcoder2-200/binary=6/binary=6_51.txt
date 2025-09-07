
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.nn.Linear()(x1)

 # Initializing the model
m = Model()
 
 # Inputs to the model
x2  = m()

# Inputs to the model
x3  = other()
 
