
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 32, kernel_size=3, padding=1)

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=1) # Concatenate the input tensor with itself along one dimension
        t2 = t1.view(t1.shape[0], -1) # Reshape the concatenated tensor to a flat vector
        t3 = torch.nn.functional.relu(t2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor

        return t3
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
