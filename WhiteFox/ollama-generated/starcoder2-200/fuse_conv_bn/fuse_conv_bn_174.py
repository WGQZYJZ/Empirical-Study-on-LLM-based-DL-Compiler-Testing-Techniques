class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 10, kernel_size=5)

    def forward(self, x1):
        output = torch.nn.functional.batch_norm(
            torch.nn.functional.conv2d(x1, self.conv))
