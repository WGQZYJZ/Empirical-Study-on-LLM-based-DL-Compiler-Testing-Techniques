
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 3, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.relu(v1)
        return v2


# Initializing the model:
m = Model()

# Input to the model
x_in = torch.randn(32, 9 * 8 * 8)
__output__  = m(x_in)

