
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 1024)
 
    def forward(self, x):
        v3= self.linear(x) 
        v4  =v3  - other 
        v5  = torch.relu(v4 )
        return v5
 
m  = Model()

