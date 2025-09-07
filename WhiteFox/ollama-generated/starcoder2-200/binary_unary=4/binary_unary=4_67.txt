
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other
        v3  = torch.relu(v2)

        return v3


m = Model()
other = torch.randn([4])
__output__  = m(torch.randn([5,2]))


