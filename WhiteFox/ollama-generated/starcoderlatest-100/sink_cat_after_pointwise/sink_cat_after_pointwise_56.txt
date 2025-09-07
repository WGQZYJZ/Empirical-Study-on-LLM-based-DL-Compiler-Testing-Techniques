
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(4, 2)
        return v2


# Inputs to the model
x1 = torch.randn(3, 2, requires_grad=True)
x2 = torch.randn(3, 2, requires_grad=True)
