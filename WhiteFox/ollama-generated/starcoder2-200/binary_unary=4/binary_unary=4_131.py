
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # pylint: disable=arguments-differ
        v2 = torch.nn.Linear(3 * 64 * 64, 5)(x1) + torch.tensor([-0.798006]) 
        v3 = self._relu(v2)
        return v3
 
    def _relu(self, x):
        return torch.clamp(x, min=0.)

m = Model()


# Inputs to the model
x1  = torch.randn(5, 3 * 64 * 64)


