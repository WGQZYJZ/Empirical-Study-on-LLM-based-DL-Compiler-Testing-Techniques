

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1)  # Apply conv 2D to the input tensor.
        v2 = torch.nn.functional.batch_norm(v1, self.running_mean, self.running_var)

# Initializing the model