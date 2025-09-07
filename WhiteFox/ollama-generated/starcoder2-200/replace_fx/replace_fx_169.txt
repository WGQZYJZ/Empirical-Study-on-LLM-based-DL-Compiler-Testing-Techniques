

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v2 = torch.nn.functional.dropout(x1, 0.3) # Dropout
        v3 = torch.rand_like(v2, dtype=torch.float64) # Generate random tensor
        return (v2 + v3).mean()

# Initializing the model
m  = Model()

