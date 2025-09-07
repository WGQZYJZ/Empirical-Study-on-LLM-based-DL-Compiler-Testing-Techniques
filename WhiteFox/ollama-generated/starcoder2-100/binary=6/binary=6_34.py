
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.zeros(x1)  # Create a zero tensor with same shape as the input of the model.
        v2  = self._get_other()
        v3 = x1 + v2 
        return v3
    @staticmethod
    def _get_other():
        # Returns 'other' used in the pattern 
        return torch.randn(1)
m  = Model()
x0  = torch.ones([1, 48])
x1 = m._get_other() - x0

