
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):  # permute
        v1 = x1.permute((0, 3))
        v2 = torch.bmm(v1, y2)  # or torch.matmul(v1, y2)

        return v2

m = Model()


# Inputs to the model