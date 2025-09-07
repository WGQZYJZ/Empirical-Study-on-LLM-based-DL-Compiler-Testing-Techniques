
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute((0, 3, 4))
        v2 = torch.bmm(v1, self.linear.weight, self.linear.bias) # or torch.matmul(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m = Model()

