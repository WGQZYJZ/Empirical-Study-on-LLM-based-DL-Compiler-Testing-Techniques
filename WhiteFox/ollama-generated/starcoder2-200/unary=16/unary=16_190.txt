
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*1048, 75)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = nn.functional.relu(v1)
 
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(30748, 32*1048)
 
__output__  = m(x1)