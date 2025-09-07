
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, x2: torch.Tensor):
        v1  = x1.permute((0, 2, 1))
        v2  = x2.permute((0, 3, 4)) # swap dimensions to compute the batch matrix product.
        v3  = torch.bmm(v1, v2)
        return v3


# Initializing the model