
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(8*7*7, 4096)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v = x1.view(-1, 3, 64, 64).contiguous().view(x1.shape[0], -1)
        q = self.conv1(v).contiguous().view(-1, 8*7*7)
        k = self.conv2(v).contiguous().view(-1, 8*7*7)
        attn_weight = torch.softmax(q @ k, dim=-1)
        return (attn_weight * v).sum(dim=1)


# Initializing the model
m = Model()


