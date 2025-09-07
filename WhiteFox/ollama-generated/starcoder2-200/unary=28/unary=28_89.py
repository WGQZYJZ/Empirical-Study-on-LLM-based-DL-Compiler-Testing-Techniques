
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v2

