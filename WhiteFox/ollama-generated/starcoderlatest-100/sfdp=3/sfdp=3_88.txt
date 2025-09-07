
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(128, 1024)
 
    def forward(self, x1, x2, x3):
        v1  = self.q(x1) # Embedding lookup of the query tensor to obtain a vector representation
        v2  = v1  * 0.5
        v3  = v1  * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4  + 1
        v6  = v2  * v5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
