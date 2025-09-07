
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 35)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_value()
        v3 = torch.relu(v2)
