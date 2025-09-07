
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 1).view(-1, 64 * 8).permute(0, 1, 3, 2) # Permute the input tensor and make some changes to it.
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 32, 8, 65) # Make some changes to the input tensor. The original input is stored in a variable and used later.

# Initial inputs for the model
v_input = x1
