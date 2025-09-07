
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      # Define the pattern, this pattern does not require any special code to be written by yourself (in this case, it requires one call to the permute method and another linear function).
      # A permutation is done on the 2nd axis of each tensor.
        return torch.nn.functional.linear(x1.permute(0, 2, 1), self.linear.weight)

# Initializing the model