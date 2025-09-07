
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.cat([x1[i] for i in range(len(x1))], dim=1)  # Concatenate all inputs along dimension 1
        return x2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
