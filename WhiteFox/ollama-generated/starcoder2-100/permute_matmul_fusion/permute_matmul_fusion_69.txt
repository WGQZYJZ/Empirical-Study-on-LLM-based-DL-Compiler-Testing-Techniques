
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t2 = x2.permute(0, 2, 1)

        t3 = t1 * t2 # Element-wise multiplication of t1 and t2
        v3 = torch.nn.functional.linear(t3, self.linear.weight, self.linear.bias)
        return v3

m = Model()

