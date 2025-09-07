class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(28 * 28, 50)
 
    def forward(self, x1):
        return self.m(x1)
