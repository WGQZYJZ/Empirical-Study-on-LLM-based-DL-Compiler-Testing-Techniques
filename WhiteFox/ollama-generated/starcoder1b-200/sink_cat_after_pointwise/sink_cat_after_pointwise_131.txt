
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # Permute the input tensor with a 3rd dimension swapped.
        v2 = v1.view(-1)
        v3 = torch.relu(v2)  # Apply pointwise unary operation (e.g., ReLU or Tanh) to reshape the tensor
        return v3


# Initializing the model
m = Model()


