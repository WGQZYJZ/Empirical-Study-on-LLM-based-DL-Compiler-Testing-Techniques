
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate x1 and x2
        v2 = self.linear1(v1)      # Apply linear transformation to concatenated tensor
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)    
x2 = torch.randn(1, 2)   
