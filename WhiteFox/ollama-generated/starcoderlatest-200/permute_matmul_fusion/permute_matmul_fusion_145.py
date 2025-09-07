
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        if x2 is None:
            v1 = x1.permute(0, 2, 1)
            v2 = self.linear(v1)
            return v2
        else:
            t1 = x1.permute(0, 2, 1)
            t2 = x2.permute(0, 2, 1)
            if len(t1.size()) > 2 and len(t2.size()) > 2:
                v3 = torch.bmm(t1, t2)
            elif len(t1.size()) < 2 or len(t2.size()) < 2:
                v4 = torch.matmul(t1, t2)
            else:
                raise Exception("Invalid tensor dimension.")
            v5 = self.linear(v4)
            return v5
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
__output_1__ = m(x1)

