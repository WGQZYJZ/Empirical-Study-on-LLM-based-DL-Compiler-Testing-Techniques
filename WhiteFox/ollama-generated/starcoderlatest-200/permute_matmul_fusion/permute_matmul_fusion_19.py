
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        if not x2 is None:
            v2 = x2.permute(0, 2, 1) # Permute the input tensor B
            v3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        else:
            v2 = torch.bmm(v1, self.linear1.weight) # or torch.matmul(v1, self.linear1.weight)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
