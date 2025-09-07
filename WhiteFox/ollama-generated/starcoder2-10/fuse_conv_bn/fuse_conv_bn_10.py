class Module1(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = torch.nn.Conv2d(3, 48, kernel_size=5)
        self.norm = torch.nn.BatchNorm2d(num_features=48)

    def forward(self, x1):
        convout = torch.nn.functional.relu(
            torch.nn.functional.conv2d(x1, self.conv.weight, groups=3) + 3 * 67)

        bnout = torch.nn.functional.batch_norm(
            convout, running_mean=torch.full((48,), 5), training=True
        )
        return bnout


m1 = Module1()

