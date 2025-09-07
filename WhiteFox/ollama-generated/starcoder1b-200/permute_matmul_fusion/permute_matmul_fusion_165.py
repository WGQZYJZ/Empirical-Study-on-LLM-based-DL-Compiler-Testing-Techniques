
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2).transpose(-2, -1)
        return torch.matmul(v2, self.linear.weight), torch.matmul(x2, self.linear.bias)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
y1 = x1.permute(0, 2, 1)  # The input tensor for the linear function will be y1
