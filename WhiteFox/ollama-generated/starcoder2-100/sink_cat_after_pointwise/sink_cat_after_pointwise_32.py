
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
         v  = torch.cat([x1, x2], dim=0)
         v2 = v.view(-1, 4)
         v3 = F.relu(v2)
         return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 2)
x2 = torch.randn(50, 2)
__output__  = m(x1, x2)
