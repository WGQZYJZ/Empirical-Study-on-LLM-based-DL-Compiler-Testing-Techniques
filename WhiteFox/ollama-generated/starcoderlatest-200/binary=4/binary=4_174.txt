
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor  # Here `other_tensor` is an input tensor (keyword argument "other")
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 32, 64, 64)
