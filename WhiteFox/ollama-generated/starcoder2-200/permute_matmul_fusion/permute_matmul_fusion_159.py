class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.matmul(
            torch.randn((3, 2)).permute(0, 2), 
            torch.randn((4, 2))).T
