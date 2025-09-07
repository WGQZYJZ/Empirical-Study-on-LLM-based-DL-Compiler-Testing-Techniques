
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3  = torch.permute(x1, 0, -1) # Swap the second and last dimension of X1
        v4  = torch.bmm(v3, x2) # Matrix multiplication between two tensors
        return v4


# Initializing the model