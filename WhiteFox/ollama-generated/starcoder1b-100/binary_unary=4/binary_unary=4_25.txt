
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(16, 8)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = (other + 0) * 0.5
        return v3

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 16)
