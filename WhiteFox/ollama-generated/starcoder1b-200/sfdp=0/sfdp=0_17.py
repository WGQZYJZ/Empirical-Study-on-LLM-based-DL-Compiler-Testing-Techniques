
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = F.softmax(self.conv(x1), dim=-1)
        v2 = torch.matmul(v1, x1)
        return v2


# Initializing the model
m = Model()


