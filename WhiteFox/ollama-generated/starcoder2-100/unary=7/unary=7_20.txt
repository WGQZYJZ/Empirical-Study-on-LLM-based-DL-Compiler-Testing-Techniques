
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1, torch.nn.Parameter(data=torch.zeros((80))))
        v3 = 6 * (v2 + 3) / torch.clamp(input=v2 + 3, min=-57.498339, max=3) 
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn((3, 6))
__output__  = m(x1)

