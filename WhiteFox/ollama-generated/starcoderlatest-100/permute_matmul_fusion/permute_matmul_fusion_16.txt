
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor A
        v2  = torch.bmm(v1, x2)   # or torch.matmul(v1, x2)
        v3  = x2.permute(0, 2, 1) # Permute the input tensor B
        return self.linear(torch.cat([v1, v2], dim=2))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 2)
x2 = torch.randn(3, 4, 4)
