
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1=0): 
        v1 = torch.nn.functional.linear(x1)
        v2 = v1 + 649 * y1 # other
        return v2


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(3, 5)
y1 = x1[:,0].mean().item()
__output__  = m(x1, y1=y1)

