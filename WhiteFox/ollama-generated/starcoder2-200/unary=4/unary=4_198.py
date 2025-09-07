
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64 * 64 * 3, 80* 32)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1   * 0.5
        v3  = v1  * 0.7071067811865476 
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2  * v5
        v7  = self.linear(v6.view(x.shape[0], -1))

        return v7

