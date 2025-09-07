
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.cat([v1 * 0.5, v1 * 0.7071067811865476], dim=-1)
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        v4 = v3 * 0.98
        v5 = self.conv2(v4)
        return v5


# Initializing the model
m = Model()

