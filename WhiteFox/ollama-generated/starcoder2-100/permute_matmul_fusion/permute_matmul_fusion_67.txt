
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
      v1 = x1.permute([0, 2, 1])
      v2 = torch.bmm(v1, v1) # or torch.matmul(v1, v1)
      return self.linear(v2).sum()


# Initializing the model
m = Model()
x1 = torch.randn([3, 4, 5]) # Input tensor A
x2 = torch.randn([3, 7, 8]) # Input tensor B
__output___ = m(torch.stack([x1]))

