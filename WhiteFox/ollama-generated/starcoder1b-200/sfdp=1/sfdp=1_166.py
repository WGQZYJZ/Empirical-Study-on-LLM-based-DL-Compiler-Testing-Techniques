
class Model(torch.nn.Module):
    def __init__(self, key_size=64):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool = torch.nn.AdaptiveAvgPool2d((key_size,))
        self.conv2 = torch.nn.Conv2d(8, 16, key_size, 1, padding=0)
        self.fc1 = torch.nn.Linear(in_features=3 * key_size, out_features=16)
 
    def forward(self, x):
        b, c, h, w = x.shape
        v1 = self.conv1(x)
        v2 = v1.view(-1, c, 1, 1)
        v3 = torch.mul(v1, 0.5)
        v4 = torch.mul(v1, 0.7071067811865476)
        v5 = torch.exp(-v4) * v2
        v6 = self.conv2(torch.mul(v5, v4))
        v7 = torch.sum(v5 * v2, dim=1)  # Compute the dot product of the dropout output and the value tensor
        return v3 + torch.log(v7)


# Initializing the model
m = Model()

