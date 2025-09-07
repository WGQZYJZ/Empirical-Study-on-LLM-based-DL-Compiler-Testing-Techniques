
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
        self.pool = torch.nn.AdaptiveAvgPool2d((1,1))
 
    def forward(self, x):
        v = self.conv1(x)
        w = self.conv2(x)
        pooled_w = self.pool(w)
        return torch.matmul(v, w) / pooled_w.pow(2).sum(dim=-1, keepdim=True)


# Initializing the model
m = Model()


