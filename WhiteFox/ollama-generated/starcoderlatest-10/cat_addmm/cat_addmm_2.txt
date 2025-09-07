
class Model(torch.nn.Module):
    def __init__(self, num_output=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(8*64*64, num_output)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        