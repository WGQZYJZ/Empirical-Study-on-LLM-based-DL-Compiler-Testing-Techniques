
class Model(torch.nn.Module):
    def __init__(self, input_dim=None, output_dim=None):
        super().__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.where(v > 0, v, -torch.log(-1 + (2 * v)) / 2)


# Inputs to the model
__input__ = torch.randn(1, 3, 64, 64)
m = Model(__input__.shape[1])
