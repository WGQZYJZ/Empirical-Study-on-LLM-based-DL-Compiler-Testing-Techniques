
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, 64)[0]
        return torch.cat([v], dim=3)


# Initializing the model
m = Model()

 # Inputs to the model
__input_tensor_1__ = torch.randn(256, 3, 96, 96)

 