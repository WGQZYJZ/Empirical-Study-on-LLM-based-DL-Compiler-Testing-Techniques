
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 2, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.cat([v1, v1], dim=-1)
        v3 = torch.cat([torch.abs(v2), v2], dim=-1)
        v4 = torch.cat([torch.exp(v3), v2 + 1], dim=-1)
        v5 = torch.nn.functional.softmax(v4, dim=-1)
        v6 = torch.mm(v5, value)
        return v6


# Initializing the model
m = Model()

