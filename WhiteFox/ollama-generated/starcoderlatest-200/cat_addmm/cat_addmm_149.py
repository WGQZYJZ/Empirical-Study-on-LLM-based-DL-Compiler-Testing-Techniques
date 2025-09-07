
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2048, 512)
        self.fc2 = torch.nn.Linear(512, 256)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = self.fc2(v1)
        v3 = torch.cat([v2], dim=0)
        return v3

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 2048, 1, 1)
