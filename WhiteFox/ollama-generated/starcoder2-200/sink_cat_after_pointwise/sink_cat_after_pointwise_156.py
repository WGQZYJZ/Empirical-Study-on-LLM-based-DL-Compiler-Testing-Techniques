
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Input shape: (batch size, seq length)
        concat = torch.cat([x1[:, -2:], x1[:, :-2]], dim=1)
        res = torch.relu(concat / 3.)
        return res


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 4096) # Batch size and sequence length (num_layers * num_directions) should be larger than or equal to 2.

# Output of the model
__output__  = m(x1)

