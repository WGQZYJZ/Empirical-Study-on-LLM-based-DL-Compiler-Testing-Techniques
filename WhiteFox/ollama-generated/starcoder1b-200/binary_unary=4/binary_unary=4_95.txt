
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 160)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other
        return v1


# Inputs to the model
input_tensor = ... # You can use a variable here.
other = ... # This value will be passed as keyword argument in forward method.


