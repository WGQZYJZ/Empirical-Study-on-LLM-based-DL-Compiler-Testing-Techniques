
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0 = [
            torch.randn(1, 3, 64, 64), 
            torch.zeros(1, 3, 64, 64)]
        __output__  = self.conv1(*v0)
