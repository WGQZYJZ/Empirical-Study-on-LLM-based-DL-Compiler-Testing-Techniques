
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other # 'other' is defined elsewhere as a constant. 
        return torch.relu(v2)


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(4, 32)
__output__  = m(x1)

