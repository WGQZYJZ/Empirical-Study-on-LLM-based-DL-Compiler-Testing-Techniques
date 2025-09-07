
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = torch.cat([x[None], x[:, :, None] * 0.5, x[:, :, None] * 0.7071067811865476,
                       x[:, :, None] * 1.2247590314525574, x[:, :, None] * 1.6482331159181112], -1)
        v = self.conv1(v) + self.conv2(v)
        return torch.nn.functional.dropout(v, p=0.7)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
