
class Model(torch.nn.Module):
    def __init__(self, num1=50472):
        super().__init__()
        self.input1 = torch.randn([num1, 3])
        self.input2 = torch.randn([num1, 3])

    def forward(self, x1):
        v1 = torch.mm(x1[0], x1[1])
        return torch.cat([v1, v1, ...], dim=0)


# Initializing the model
m = Model()

# Inputs to the model
x1  = (torch.randn(256), torch.randn(256))
__output__  = m(x1)