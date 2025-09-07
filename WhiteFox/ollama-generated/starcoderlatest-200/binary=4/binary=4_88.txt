
class Model(torch.nn.Module):
    def __init__(self, input_shape, hidden_dim=8):
        super().__init__()
        self.linear = torch.nn.Linear(*input_shape, 1)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model((3, 64, 64))

# Inputs to the model
other_tensor = torch.randn(8, 100, device="cuda")
x1 = torch.randn(1, 3, 64, 64)
