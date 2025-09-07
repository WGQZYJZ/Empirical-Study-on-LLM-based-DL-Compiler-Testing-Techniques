
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 + inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Inputs to the model
x1 = torch.randn(1024, 32)
inp = x1 * -1  # We use negative values as inputs so that we can see which lines will be executed by symbolic differentiation and which won't.
