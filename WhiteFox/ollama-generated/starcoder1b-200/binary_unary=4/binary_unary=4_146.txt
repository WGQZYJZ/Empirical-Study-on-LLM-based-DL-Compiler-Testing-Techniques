
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 512)
 
    def forward(self, x1, other=None):
        if other is not None:
            x2 = self.linear(x1) + other  # Use the result of linear transformation
        else:
            x2 = self.linear(x1)
        return relu(x2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
