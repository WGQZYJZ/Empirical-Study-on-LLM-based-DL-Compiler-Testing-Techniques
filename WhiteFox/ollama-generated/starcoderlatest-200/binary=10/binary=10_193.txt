
class Model(torch.nn.Module):
    def __init__(self, out_features=10):
        super().__init__()
        self.linear = torch.nn.Linear(3, out_features)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v6

