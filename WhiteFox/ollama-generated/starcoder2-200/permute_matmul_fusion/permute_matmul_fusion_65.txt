
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):  # Notice that we don't permute here!
        v3 = torch.bmm(x1, y2) # or torch.matmul(y1, x2), this is not the case here
        return v3


# Initializing the model