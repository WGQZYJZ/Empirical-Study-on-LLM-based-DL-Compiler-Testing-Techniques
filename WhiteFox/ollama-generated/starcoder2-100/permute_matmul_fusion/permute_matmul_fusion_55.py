
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, y1, x2):
        v1  = x1.permute(0, 3, 1, 2).contiguous() # This permute is not used.
        v2  = x2.permute(0, 2, 1) 
        v4  = torch.bmm(v2, y1)

        return self.linear(v4)


# Initializing the model
m = Model()
x1, x2 = torch.randn(3, 5, 2), torch.randn(60, 78, 9)
__output__  = m(x1, x1, x2)


