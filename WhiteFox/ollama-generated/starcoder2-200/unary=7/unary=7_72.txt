
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3,8)
 
    def forward(self, x2):
        v7  = self.linear1(x2)
        v8  = v7 * clamp(min=0, max=6, v7 + 3) / 6 
        return v8


# Initializing the model
m  = Model()

# Inputs to the model
x2  = torch.randn(1, 3)
 
__output__  = m(x2)
