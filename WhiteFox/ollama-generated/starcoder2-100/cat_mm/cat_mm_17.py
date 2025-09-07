
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim

    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2)
        v2  = torch.cat([v1 for _ in range(self.dim)], self.dim)
        return v2

# Initializing the model with dim=4:
m  = Model(4)
__output___  = m(torch.randn(3, 3), torch.randn(3, 5))

