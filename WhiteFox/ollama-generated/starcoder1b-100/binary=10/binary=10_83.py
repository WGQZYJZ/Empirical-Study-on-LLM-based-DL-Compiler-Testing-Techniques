
class Model(torch.nn.Module):
    def __init__(self, n_input, n_output):
        super().__init__()
        self.linear = torch.nn.Linear(n_input, n_output)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = other  # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model(3, 64)
__input__ = torch.randn(1, 3, 64, 64)
v1 = m(__input__)

