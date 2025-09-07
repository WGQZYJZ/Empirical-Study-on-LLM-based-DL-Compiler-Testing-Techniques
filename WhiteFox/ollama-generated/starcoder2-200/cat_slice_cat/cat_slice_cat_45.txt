

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, *inputs):
      # Initialize an empty list of tensors.
      xs = []
      for x in inputs:
          # Append each input to the list of tensors.
          xs += [x]
      # Concatenate tensors along dimension 1 and return.
      return torch.cat(xs, dim=1)


# Initializing the model
m  = Model()


# Inputs to the model

x0 = torch.randn(256, 3, 64, 64)

x1 = torch.randn(257, 3, 64, 64)
