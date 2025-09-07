
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size=2**64-1):
        v1 = torch.cat([x1, x1], dim=1)
        v2 = v1[:, 0:size]
        return v2


# Input tensor of the model
input_tensor = torch.randn(1, 3, 64, 64)
