
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = x1[:, :9223372036854775807]
        v2 = torch.cat([x1, v1], dim=1)  # Concatenate the original tensor along dimension 1 and the sliced tensor along dimension 1
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
