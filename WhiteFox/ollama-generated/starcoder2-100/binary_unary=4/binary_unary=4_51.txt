
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(20,1)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        v2  = v1 + other # If the `other` argument is None then it becomes a dummy
        v3  = torch.relu(v2)
        return v3
