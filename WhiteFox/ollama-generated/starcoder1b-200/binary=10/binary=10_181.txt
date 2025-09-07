
class Model(torch.nn.Module):
    def __init__(self, other=100):
        super().__init__()
        self.linear = torch.nn.Linear(16, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # Apply a linear transformation to the input tensor plus another value "other"
        return v1


# Initializing the model
m = Model()


