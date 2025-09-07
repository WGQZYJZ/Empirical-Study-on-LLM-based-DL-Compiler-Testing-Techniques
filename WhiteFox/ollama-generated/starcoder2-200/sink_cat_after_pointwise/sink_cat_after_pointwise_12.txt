
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()

        self.dim = dim

    def forward(self, x1, x2):
        t0  = torch.cat([x1, x2], dim=self.dim) # Concatenate the input tensors along 'dim' dimension
        t1  = t0.view(-1, ...) # Reshape the concatenated tensor
        t2  = torch.nn.functional.relu(t1) # Apply a pointwise unary operation to the reshaped tensor (e.g., ReLU or Tanh)

        return t2


# Initializing the model with argument dim = 0:
m  = Model(dim=0)
x1, x2 = torch.randn(3,4), torch.randn(5,4)
__output__  = m(x1, x2).shape # Reshape the concatenated tensor before applying ReLU to the reshaped tensor


# Initializing the model with argument dim = 1:
m  = Model(dim=1)
x1, x2 = torch.randn(3,4), torch.randn(5,4)
__output__  = m(x1, x2).shape # Reshape the concatenated tensor before applying ReLU to the reshaped tensor


# Initializing the model with argument dim = 0:
m  = Model(dim=0)
x1, x2 = torch.randn(3,4), torch.randn(5,4)
__output__  = m(x1, x2).shape # Reshape the concatenated tensor before applying ReLU to the reshaped tensor

