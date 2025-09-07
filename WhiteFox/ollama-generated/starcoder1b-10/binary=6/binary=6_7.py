
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 1  # Subtract '1' from the output of the linear transformation
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(3, 4)  # A sample input tensor
