
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(in_features=64 * 64 * 8, out_features=1024)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = F.relu(v1.view(-1))
        return self.linear(v2)


# Inputs to the model
x = torch.randn(32, 3, 64, 64)
