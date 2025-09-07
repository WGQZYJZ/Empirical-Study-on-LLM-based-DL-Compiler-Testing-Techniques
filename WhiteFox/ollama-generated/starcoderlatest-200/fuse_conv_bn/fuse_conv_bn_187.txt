
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 1, kernel_size=(4,2), stride=4)

    def forward(self, x1):
        v1 = F.pad(x1, (0,0,0,0,4,0))
        v2 = self.conv(v1)
        output = F.batch_norm(v2, 32)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 24, 36)
