
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v2 = torch.clamp_min(x1  +  3, min=0)
         v4 = torch.clamp_max(v2, max=6)
         return (v4 / 6).type('torch.FloatTensor')


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(10)
 
