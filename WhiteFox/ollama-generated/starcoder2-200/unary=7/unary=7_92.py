
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(7, 1024)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * clamp(min=0, max=6, v1 + 3) # We added a +3 here to make the model different from the previous one
        v3  = v2 / 6
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(7)
__output__  = m(x1)