

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(80, 12)
 
    def forward(self, x1): 
        v1 = torch.flatten(x1, start_dim=1) 
        v3 = torch.relu(v1 - other) # The 'other' value is fixed and can be found at:
        return v3

# Initializing the model
m  = Model()

