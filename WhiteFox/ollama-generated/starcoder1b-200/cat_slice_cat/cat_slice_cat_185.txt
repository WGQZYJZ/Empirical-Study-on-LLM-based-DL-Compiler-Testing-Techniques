
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat(x1, dim=1)
        v2 = v1[:, :, :9223372036854775807]  # Get slice of the concatenated tensor along dimension 1
        v3 = v2[:, :, :9223372036854775807]  # Further slice of the tensor along dimension 1
        return torch.cat([v1, v3], dim=1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
