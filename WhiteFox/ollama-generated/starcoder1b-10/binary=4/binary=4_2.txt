
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # Apply a linear transformation to the input tensor and then add another tensor (specified by the keyword argument "other")
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32)
