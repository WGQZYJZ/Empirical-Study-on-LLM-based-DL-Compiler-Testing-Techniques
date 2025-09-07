
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.mm(x1, x2) + 50
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model
__inputs__  = [torch.randn(3, 4),
              torch.randn(4, 5)]

m(*__inputs__)
