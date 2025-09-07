
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320 * 15, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor
        return v1


# Initializing the model and assigning a constant value to "other_tensor"
m = Model()
other_tensor = torch.zeros([320 * 15])
 
# Inputs to the model (a randomly generated tensor of shape [batch size, input dimensionality] with values in range(-10, 10))
x1 = torch.randn(4, 320 * 15)


