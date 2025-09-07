
class Model(nn.Module):
    def __init__(self, hidden_size=10):
        super().__init__()
        self.fc = nn.Linear(hidden_size + 2, 5)
 
    def forward(self, x):
        v = torch.cat([x, x, x, x, x], dim=-1)
        v = v.view(v.shape[0] // 2)
        v = self.fc(v)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 10)
x2  = torch.randn(4, 10)
