
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return 0.5 * torch.cumsum(x, dim=2, keepdim=True)

 # Inputs to the model
x = torch.randn(1, 3, 64, 64)
