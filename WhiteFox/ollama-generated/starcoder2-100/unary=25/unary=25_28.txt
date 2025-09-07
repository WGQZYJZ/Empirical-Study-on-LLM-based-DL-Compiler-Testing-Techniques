
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.randn(32, 7)  # Dummy input for the linear transformation in forward function
        v1 = self._lrelu(v0)

        return v1

    @staticmethod
    def _lrelu(v0):
        v1  = 5 * v0
        v2  = v1 > 0
        v3  = torch.where(v2, v1, -v1)
        return v3


# Initializing the model
m  = Model()
