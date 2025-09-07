
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate the input tensors along axis=1
        v2 = v1.view(v1.size(0), -1)  # Reshape v1 to (batch_size * num_channels, num_elements_per_channel)
        v3 = torch.relu(v2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 4)  # batch_size=2, channels=2, elements_per_channel=4
x2 = torch.randn(2, 5, 3)  # batch_size=2, channels=5, elements_per_channel=3
