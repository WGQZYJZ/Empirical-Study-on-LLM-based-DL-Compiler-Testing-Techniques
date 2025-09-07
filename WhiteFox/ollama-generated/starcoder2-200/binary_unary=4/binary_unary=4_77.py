

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.Linear()(x)
        v2  = v1 + torch.zeros(3, 5).to(v1) # other is an arbitrary tensor that will be passed as a keyword argument 
        v3  = torch.nn.ReLU()
        
        return v3

# Initializing the model