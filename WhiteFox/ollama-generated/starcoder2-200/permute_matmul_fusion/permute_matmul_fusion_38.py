
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        # First example, permuted tensor A and B is used for the bmm operation
        v1  = x1.permute(0, 2, 1)
        v2  = x2.permute(0, 3, 2, 1)
        v3  = torch.bmm(v1, v2).permute(0, 2, 3, 1) # permute the output tensor

        # Second example, permuted tensors B and A are used for the bmm operation
        v4  = x2.permute(0, 3, 2, 1)
        v5  = x1.permute(0, 2, 1)
        v6  = torch.bmm(v4, v5).permute(0, 2, 3, 1) # permute the output tensor

        # Third example, permuted tensors B and A are used for the matmul operation
        v7  = x2.permute(0, 3, 2, 1)
        v8  = x1.permute(0, 2, 1)
        v9  = torch.matmul(v7, v8).permute(0, 2, 3, 1) # permute the output tensor

        return (v3 + v6 + v9).sum()
