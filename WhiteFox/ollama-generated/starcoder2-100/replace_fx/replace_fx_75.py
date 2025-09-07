
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v2 = torch.rand_like(x1, dtype=torch.float32) # Generate a random tensor with the same size as `x1` filled with float 32 numbers.
      v4 = torch.nn.functional.dropout(v2, p=0.5)    # Apply dropout to this generated tensor
      return v4


# Initializing model
m  = Model()


# Inputs to the model