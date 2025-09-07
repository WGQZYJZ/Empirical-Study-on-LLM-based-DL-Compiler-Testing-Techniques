
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 3)
        self.linear_2 = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).contiguous().view(-1, 2 * 3).permute(0, 2, 1) # Permute the input tensor A
        v2 = x2.permute(0, 2, 1).contiguous().view(-1, 2 * 3).permute(0, 2, 1) # Permute the input tensor B
        v3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
