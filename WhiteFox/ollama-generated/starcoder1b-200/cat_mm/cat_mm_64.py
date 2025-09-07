
class Model(nn.Module):
    def __init__(self, n: int = 2):
        super().__init__()
        self.linear1 = nn.Linear(n * 2, n) # [input_size, output_size]
        self.linear2 = nn.Linear(n, n)
 
    def forward(self, x: torch.Tensor):
        x1, x2 = torch.chunk(x, chunks=2, dim=0)
        x3 = torch.cat([x1, x1, ..., x1], 0) # [input_size, input_size * n]
        x4 = self.linear1(x3)
        x5 = self.linear2(x4)
        return x5


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 100, requires_grad=True)
input1, input2 = x1[:, None], x1[:, None]
