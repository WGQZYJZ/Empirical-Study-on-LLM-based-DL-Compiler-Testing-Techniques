
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # [N, H, W, C] => [C, N, H, W]
        v2 = self.linear(v1)  # [C, N, H, W] => [N, H, W, C]
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
