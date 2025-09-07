
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor # The second tensor in the pattern is now stored as `other_tensor` and will be added to v1.
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(8, 3) # Any other random tensor (specified by the keyword argument "other") that is compatible with the input of linear layer.
other_tensor = torch.randn(200, 4)


