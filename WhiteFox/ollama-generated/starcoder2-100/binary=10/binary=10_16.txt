
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self._other + torch.ones(x1.size()) # pylint: disable=E0621
        return self._linear_layer(x1)  + v2

# Initializing the model
m  = Model()
 
# Inputs to the model
__input__ = torch.randn(8, 32)

