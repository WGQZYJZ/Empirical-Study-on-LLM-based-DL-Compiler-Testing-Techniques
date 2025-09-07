
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v2  = self.linear(x1)
        v3  = v2 + other 
        v4  = nn.functional.relu(v3)  
        return v4


# Initializing the model
other  = torch.randn(5)
m  = Model()
 
# Inputs to the model
x1  = torch.randn(60, 10)
__output__  = m(x1)