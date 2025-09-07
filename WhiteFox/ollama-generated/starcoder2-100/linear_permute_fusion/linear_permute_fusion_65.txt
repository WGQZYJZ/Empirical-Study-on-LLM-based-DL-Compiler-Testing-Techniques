
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v3  = self.linear(x1).permute(-1, -2) # Permute the output of the linear function with one less than the original dimensions.
        return v3


# Initializing the model
m = Model()

# Input to the model
x1 = torch.randn(4, 4)
__output__  = m(x1)

