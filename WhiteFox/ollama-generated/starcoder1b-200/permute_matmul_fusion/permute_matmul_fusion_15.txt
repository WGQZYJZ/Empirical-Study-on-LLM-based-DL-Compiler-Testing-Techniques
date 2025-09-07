
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.bmm(v1, x2) if self._use_matmul else torch.bmm(x1, v2) # If use matmul (e.g., if the shape of x1 is [C, H*W]), return matmul; otherwise return bmm
        return v2


# Initializing the model
m = Model()


