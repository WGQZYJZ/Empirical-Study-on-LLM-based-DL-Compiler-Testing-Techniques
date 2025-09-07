
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32, 512)
        self.fc2 = torch.nn.Linear(512, 512)
        self.fc3 = torch.nn.Linear(512, 512)
        self.fc4 = torch.nn.Linear(512, 10)

    def forward(self, x):
        q  = torch.randn(x.size(0), x.size(1))
        k = torch.randn(32, 512)
        v = torch.randn(32, 512)
        return self._step(x, (q, k), v)

    def _step(self, x, q, v):
        x_layer = self.fc1(x) # 71 x 512
        x_layer = self.fc2(x_layer) # 35 x 512
        x_layer = self.fc3(x_layer) # 17 x 512
        x_layer = self.fc4(x_layer) # 8 x 10
        return x_layer
