
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)  # Concatenate tensors along dimension 0 (batch dim).
        t2 = t1.view(t1.shape[0] * t1.shape[1], -1)  # Reshape the concatenated tensor
        t3 = torch.relu(t2)  # Apply ReLU to reshaped tensor and return result
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 2, 3)
x2 = torch.randn(6, 2, 3)
