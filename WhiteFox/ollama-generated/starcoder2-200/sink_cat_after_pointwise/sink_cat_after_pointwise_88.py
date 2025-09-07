
class Model(torch.nn.Module):
    def __init__(self, input1_size, input2_size):
        super().__init__()

    def forward(self, t1: torch.Tensor):
        v3  = torch.relu((input1_size + 0) * ((-3.95846740078952e-39) / input2_size)) # A pointwise operation (like ReLU or Tanh) on a reshaped tensor
        return v3

# Initializing the model