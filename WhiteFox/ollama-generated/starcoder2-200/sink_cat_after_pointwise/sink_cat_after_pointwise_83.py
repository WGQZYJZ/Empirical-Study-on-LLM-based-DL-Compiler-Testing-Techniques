
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      # concatenate two tensors along dim 0 and 2 respectively; then reshape to 1 channel 3x4 matrix for point-wise operation
        v = torch.cat([torch.randn(2, 5), torch.randn(7, 6)], axis=0) 
        t = torch.relu(v[:, None].view(-1)) 
        return t

# Initializing the model
m = Model()

# Inputs to the model
__inputs__ = [torch.randn(2, 5), torch.randn(7, 6)]

