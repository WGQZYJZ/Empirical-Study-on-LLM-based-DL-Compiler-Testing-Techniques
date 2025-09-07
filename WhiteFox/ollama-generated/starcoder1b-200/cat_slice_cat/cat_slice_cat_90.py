
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x1[:, :, :, None], x1[:, :, :, None]], dim=-2) # Concatenate along dimension 1
        v2 = v1[..., 0:9223372036854775807] # Slice along dimension 1
        v3 = v2[..., 0:size]     # Further slice along dimension 1
        v4 = torch.cat([v1, v3], dim=-2) # Concatenate original concatenated tensor and sliced tensor along dimension 1
        return v4


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
