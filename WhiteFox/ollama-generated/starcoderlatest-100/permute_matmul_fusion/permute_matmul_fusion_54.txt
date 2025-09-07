
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1) # permute the input tensor A
        t2 = x2.permute(0, 2, 1) # permute the input tensor B
        v1 = torch.bmm(t1, t2)
        v2 = torch.matmul(v1, self.linear.weight) + self.linear.bias
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 2, 3)
