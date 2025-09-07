
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3  = torch.bmm(x1.permute(0, 2, 1), x2)  # or you can use torch.matmul(x1.permute(0, 2, 1), x2)

        return v3


# Initializing the model