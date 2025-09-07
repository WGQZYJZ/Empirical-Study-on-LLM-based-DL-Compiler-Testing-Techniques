
class Model(torch.nn.Module):
    def __init__(self, other_tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if other_tensor is not None:
            v2 = v1 + other_tensor
        else:
            # Add the constant to avoid error in JIT compilation
            # https://discuss.pytorch.org/t/how-to-use-the-constant-0-with-jit-scripting/75343/16
            torch._C._set_default_dtype(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model with other tensor passed as keyword argument
x1 = torch.randn(1, 3, 64, 64)
other_tensor = torch.full((1, 8), 0.75).to('cpu') # To run in CPU only mode to avoid JIT compilation error
