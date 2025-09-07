
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc    = torch.nn.Linear(8 * 64 * 64, 256)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1.view(-1, 8 * 64 * 64)
        v3 = torch.mm(v2, torch.Tensor([[0.05]])).view(-1, 1, 1, 256).repeat((1, v2.shape[1], 1, 1))
        v4 = torch.cat([v3, v2], dim=1)
        v5 = torch.mm(torch.sigmoid(self.fc(v4)), x)
        return v5


# Initializing the model
m = Model()


