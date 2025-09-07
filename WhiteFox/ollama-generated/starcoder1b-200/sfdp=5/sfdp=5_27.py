
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.fc    = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        w1 = F.linear(v1, nn.Parameter(torch.randn(w1.size(0), w1.size(1))))
        w2 = F.linear(v1, nn.Parameter(torch.randn(w2.size(0), w2.size(1))))
        x1 = torch.mm(x1, w1)
        x2 = torch.matmul(x1, w2)
        # v3 = self.fc(F.linear(v1, nn.Parameter(torch.randn(w3.size(0), w3.size(1)))))
        # v4 = torch.mm(x1, w3)
        return x2

