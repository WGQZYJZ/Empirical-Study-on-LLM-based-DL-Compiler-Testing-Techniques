
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v1 = torch.nn.functional.linear(x1) # Apply linear transformation to input tensor
      return v1 + torch._C._debug_get_variable_state('other', dtype=torch.float32).data

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 4)

