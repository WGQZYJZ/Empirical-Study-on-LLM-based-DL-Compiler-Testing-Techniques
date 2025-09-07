
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         return torch.ops.aten.matmul(x1, torch.randn((4096, 37)))


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(800)
