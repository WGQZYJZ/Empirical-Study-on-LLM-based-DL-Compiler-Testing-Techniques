
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        #v3 = self.linear(v1).bmm(v2)   # A or B or C as the pattern of invoking the torch.bmm function on a permuted tensor with more than two dimensions.
        v4 = torch.matmul(self.linear(v1), v2)    # or B or C as the pattern of invoking the torch.matmul function on a permuted tensor with more than two dimensions.
        return v4

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
