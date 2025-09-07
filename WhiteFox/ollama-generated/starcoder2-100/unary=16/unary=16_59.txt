
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(3*1024, 8)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = F.relu(v1)
