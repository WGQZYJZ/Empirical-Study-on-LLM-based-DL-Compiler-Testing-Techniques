
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.bmm(x1, x2) # Or torch.matmul(x1, x2), etc.


# Initializing the model