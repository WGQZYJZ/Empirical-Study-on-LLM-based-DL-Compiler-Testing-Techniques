
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.relu(x1)
        v2  = v1.permute(0, 2, 1) # Permute the input tensor to convert a shape [N, H*W, 2] into [N, W, H]
        v3  = self.linear(v2)     # Apply linear transformation to the permuted tensor.
        return v3


# Initializing the model