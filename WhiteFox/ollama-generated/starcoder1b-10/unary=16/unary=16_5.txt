
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32 * 64, 50)
        self.relu = torch.nn.ReLU()
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, x1):
        v1 = torch.flatten(x1, start_dim=-1, end_dim=-2)
        v2 = self.fc1(v1)
        v3 = self.relu(v2)
        v4 = self.dropout(v3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64 * 64, dtype=torch.double)
