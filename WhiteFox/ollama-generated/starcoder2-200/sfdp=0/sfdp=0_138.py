
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled = 8
        self.key = torch.nn.Parameter(torch.randn(3, 10))
        self.query = torch.nn.Parameter(torch.randn(3, 7))
 
    def forward(self, x):
        v1 = torch.matmul(self.query, self.key) / math.sqrt(8)
        v2 = v1.softmax(dim=-1)
        return v2
 
m = Model()

