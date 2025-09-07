
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.split(x1, 32) + [x1[-i] for i in range(-len(x1)+1, 0)]

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8*512)
 
m(x1)

