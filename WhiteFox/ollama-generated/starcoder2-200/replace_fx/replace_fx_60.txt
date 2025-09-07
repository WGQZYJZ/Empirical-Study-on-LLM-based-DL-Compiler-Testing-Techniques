

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, p=0.2)
        v2  = torch.rand_like(v1, dtype=torch.float32)

# Initializing the model
m  = Model()

# Inputs to the model 
x1 = torch.randn(4, 5) # Input of shape (4, 5). The function rand_like uses a random tensor of the same shape and dtype as an input parameter
