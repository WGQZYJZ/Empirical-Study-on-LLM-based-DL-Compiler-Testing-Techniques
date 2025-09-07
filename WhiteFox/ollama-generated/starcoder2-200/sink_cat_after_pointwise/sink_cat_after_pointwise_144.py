
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v0 = torch.rand(2) # Generate a random vector of size 2
      v1 = self._get_vector(v0) # Apply a non-linear operation to the vector and obtain another vector. The function `_get_vector` is hidden from users (e.g., it might be a private method, an attribute or a function imported using `from utils import *`).
      v2 = torch.nn.functional.tanh(v1) # Apply another pointwise unary operation on the first obtained tensor to obtain the final output.
      return x1, v0


# Initializing model