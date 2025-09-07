
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.split(x1, (3, 2), dim=-1)
        v2 = v1[0] * 2 + v1[1]  # Divide both tensors along the last dimension
        v3 = torch.cat([v1[i] for i in range(len(v1))], dim=-1) * 3.0 + v2 + 1  # Concatenate the split tensors along the same dimension
        return v3
