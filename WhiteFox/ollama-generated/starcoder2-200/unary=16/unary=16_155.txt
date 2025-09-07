
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1  = torch.nn.Linear(32768, 4)
 
    def forward(self, x1):
        v1  = torch.relu(x1 @ self.weight +  self.bias)
