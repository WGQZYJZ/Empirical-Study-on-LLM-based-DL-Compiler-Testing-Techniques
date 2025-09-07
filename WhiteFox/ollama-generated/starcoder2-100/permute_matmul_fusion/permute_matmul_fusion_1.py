class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v0 = torch.randn(3)
        v1  = self.func_1(v0) # call a function
        v2  = x1.permute(0, 2, 1)
        v3 = torch.nn.functional.linear(v2, ...)
        v4 = y1 / (self.func_2(y1)) * self.func_3(y1)

        return v3
