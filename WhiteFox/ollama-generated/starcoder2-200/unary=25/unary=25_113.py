
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear  = torch.nn.Linear(64*64*8, 512)
 
    def forward(self, x):
        v1  = linear(x)
        v2  = t2 > 0
