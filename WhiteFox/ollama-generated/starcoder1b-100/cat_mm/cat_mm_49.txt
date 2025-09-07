
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2):
        super().__init__()
        self.dim1 = dim1
        self.dim2 = dim2
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1 for i in range(0, self.dim1)], dim=0)  # Concatenate `x1` along dimension 0
        v2 = torch.cat([x1 for i in range(0, self.dim1)], dim=0)  # Concatenate `x1` along dimension 0
        v3 = x1 * x1
        v4 = v1 + v2
        v5 = v3 - v4
        return torch.cat([v1, v5], dim=-1)


# Initializing the model
m = Model(dim1=3, dim2=2)


