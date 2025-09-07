
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(7 * 7 * 8, 256)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 7 * 7 * 8)
        v2 = self.linear(v1)
        return relu(t2)


# Initializing the model
m = Model()

