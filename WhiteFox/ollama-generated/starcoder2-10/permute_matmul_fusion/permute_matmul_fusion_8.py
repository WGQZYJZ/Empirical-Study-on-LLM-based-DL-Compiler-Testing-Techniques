
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.bmm(x1.permute(0, 2, 1), x2) # Permute the input tensor A and B
        v2  = torch.bmm(v1, x2.permute(0, 2, 1)) # Swap the last two dimensions of the permuted tensor B
        return v2


# Initializing the model