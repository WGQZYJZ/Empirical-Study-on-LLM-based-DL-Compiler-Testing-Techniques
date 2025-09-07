
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v2 = torch.bmm(v1, x2)   # or torch.matmul(v1, x2), Permute the input tensor B
        return self.linear1(v3)


# Initializing the model