
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2=None):
        if x2:  # Only the first argument `x2` should be passed to `forward`
            t = torch.cat([tensor1, tensor2], dim=...)
            return torch.relu(t)  # The `forward` function is called with a default value of `None`.
