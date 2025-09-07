
class Model(torch.nn.Module):
    def __init__(self, num_layers):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        for i in range(num_layers - 1):
            setattr(self, 'fc%d' % i, torch.nn.Linear(7 * 7 * 8, 50))
        setattr(self, 'fc%d' % (num_layers - 1), torch.nn.Linear(7 * 7 * 8, 1))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        for i in range(len(self.__class__.__dict__) - 2):
            func = getattr(self, 'fc%d' % i)
            v1 = func(v1.view(-1, 7 * 7 * 8))
 
        v6 = self.fc(v1.view(-1, 7 * 7 * 8))
        return v6


# Initializing the model
m = Model(num_layers=5)
x1 = torch.randn(1, 3, 64, 64)
