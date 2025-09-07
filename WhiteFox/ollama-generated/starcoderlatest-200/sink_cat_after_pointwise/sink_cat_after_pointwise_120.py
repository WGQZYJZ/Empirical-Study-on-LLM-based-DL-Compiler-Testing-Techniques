
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=0)  # Concatenate the tensors along the first dimension
        v2 = v1.view(v1.size()[0], -1) # Reshape the concatenated tensor to [n, h * w * c] where n is the batch size and h, w, and c are determined by the sizes of x1, x2, and x3 respectively
        v3 = torch.relu(v2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Inputs to the model
x1 = torch.randn(10, 2, 2)
x2 = torch.randn(10, 4, 2)
x3 = torch.randn(10, 8, 2)
