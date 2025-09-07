
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2=None):
        if x2 is None:
            v1 = x1.permute(0, 2, 1).contiguous()
            v2 = torch.bmm(v1, v1.permute(0, 2, 1))
        else:
            t1 = x1.permute(0, 2, 1) # Permute the input tensor A
            t2 = x2.permute(0, 2, 1) # Permute the input tensor B
            v1 = torch.matmul(t1, t2)
        return self.linear(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 2, 3)
