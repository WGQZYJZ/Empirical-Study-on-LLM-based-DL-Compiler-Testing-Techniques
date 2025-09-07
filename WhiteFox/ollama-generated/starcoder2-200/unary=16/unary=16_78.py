
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(512, 8096)
__output__  = m(x1)


