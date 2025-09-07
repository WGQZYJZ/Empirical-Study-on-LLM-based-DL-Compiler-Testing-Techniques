
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key = torch.nn.Linear(3, 8)
        self.value = torch.nn.Linear(3, 8)
 
    def forward(self, x1, x2):
        v1 = self.query(x1).unsqueeze(-2) @ self.key(x2).transpose(-2, -1) / math.sqrt(self.query.out_features) + torch.nn.functional.softmax(x3, dim=-1)
        v2 = v1 @ self.value(x2).transpose(-2, -1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
