
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 8, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + 5  # Add a constant (specified by the keyword argument "other") to the output of the linear transformation
        return v2


# Initializing the model
m = Model()


