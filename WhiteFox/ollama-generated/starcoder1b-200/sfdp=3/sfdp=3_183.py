
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1) * 0.5
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        qk = torch.matmul(v1, v3.transpose(-2, -1)) * 0.01
        v5 = torch.softmax(qk, dim=-1) * 0.9
        output = v4 * v5
        return output


# Initializing the model
m = Model()


