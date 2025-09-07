
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 3)
        self.key = torch.nn.Linear(5, 4)
 
    def forward(self, x1):
        v1 = self.query(x1)
        v2 = v1 @ self.key.transpose(-1, -2) / math.sqrt(v1.size(-1))
        v3 = torch.softmax(v2, dim=-1)
        v4 = v3  * x1
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 5, 64, 64)
