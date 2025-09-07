
class Model(torch.nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.conv = torch.nn.Linear(input_dim + 1, 8)
 
    def forward(self, x):
        v  = self.conv(x)
        return v


# Inputs to the model
__inputs__ = [torch.randn(1, 3), torch.randn(2, 4), ...]
