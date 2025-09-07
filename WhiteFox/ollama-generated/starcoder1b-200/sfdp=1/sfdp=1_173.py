
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 512)
 
    def forward(self, x1):
        m  = self.linear(x1)
        