
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)  # A -> B
        v2 = torch.bmm(v1, x2)      # B -> AB

        return v2


# Inputs to the model
x1 = torch.randn(3, 2, 5)
y1 = torch.randn(3, 2, 7)
