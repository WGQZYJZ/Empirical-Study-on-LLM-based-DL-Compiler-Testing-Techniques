
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l1 = self.linear()(x1)
        l2 = l1 * F.clamp(min=0, max=6, input=l1 + 3) / 6
        return l2


# Initializing the model
m  = Model()
 
 # Inputs to the model
 x1  = torch.randn(5, 8)
 
 
__output__  = m(x1)
