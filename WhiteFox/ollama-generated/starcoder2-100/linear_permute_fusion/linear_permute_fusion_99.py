
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        v2 = self.linear(x1).permute(-1, -2) # Permute the output tensor from the linear transformation.
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(50, 30, 40)
