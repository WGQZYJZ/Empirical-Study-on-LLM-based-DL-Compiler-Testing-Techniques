
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0, bias=False)
    
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5 + 1
        w = self.conv2(v2).transpose(-2, -1)
        w = torch.softmax(w, dim=-1)
        return w @ x1


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
