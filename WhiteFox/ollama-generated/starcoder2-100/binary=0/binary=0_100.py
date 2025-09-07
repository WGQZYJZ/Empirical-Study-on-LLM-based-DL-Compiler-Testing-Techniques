
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

        # Add the other tensor to conv's output in the model initialization procedure
        self.other = other

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other  # This tensor is passed as a keyword argument when initializing the Model class

        return v2

# Initializing the model
m  = Model(torch.randn(3,8))


# Inputs to the model