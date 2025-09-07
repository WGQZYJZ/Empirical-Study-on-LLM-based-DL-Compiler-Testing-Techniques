

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear(x1.shape[-1], 8)(x1) 
        v2 = v1 + torch.randn_like(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model