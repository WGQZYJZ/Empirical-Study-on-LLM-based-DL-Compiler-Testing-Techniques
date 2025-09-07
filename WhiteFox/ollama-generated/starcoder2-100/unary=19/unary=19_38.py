
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(576*28*28 + 512, 1)
 
    def forward(self, x1):
        v1 = self.conv_first(x1).flatten()
