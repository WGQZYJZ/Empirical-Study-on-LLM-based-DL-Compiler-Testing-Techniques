
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = F.relu(v1) 
        return v2
 
m = Model()

