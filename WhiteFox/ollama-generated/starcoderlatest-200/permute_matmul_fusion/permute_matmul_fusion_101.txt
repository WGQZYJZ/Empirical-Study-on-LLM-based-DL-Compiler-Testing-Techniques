
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        if x2 is not None:
            t3 = torch.bmm(x1, x2) # or torch.matmul(x1, x2)
        else:
            t1 = x1.permute(0, 2, 1) # Permute the input tensor A
            t2 = x2.permute(0, 2, 1) # Permute the input tensor B
            t3 = torch.bmm(t1, t2) # or torch.matmul(t1, t2)
        v1 = torch.nn.functional.linear(t3, self.linear.weight, self.linear.bias)
        return v1


# Inputs to the model
x1 = torch.randn(1, 2, 2)
