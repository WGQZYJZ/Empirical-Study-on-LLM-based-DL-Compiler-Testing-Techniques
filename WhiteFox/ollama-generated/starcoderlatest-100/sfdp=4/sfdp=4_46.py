
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.query(x1) @ self.key.transpose(-2, -1).unsqueeze(dim=0).unsqueeze(dim=-1) / math.sqrt(v1.size(-1)) + 1
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 32, 5000, 5000)
