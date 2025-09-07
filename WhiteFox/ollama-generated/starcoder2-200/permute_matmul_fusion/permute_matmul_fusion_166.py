
class Model(torch.nn.Module):
    def __init__(self, A, B):
        super().__init__()
        self.linear1 = torch.nn.Linear(A[0], A[0])
        self.linear2 = torch.nn.Linear(B[0], B[0])

    def forward(self, x1, x2):
        v1  = x1.permute([0, len(x1.shape)-1] + list(range(len(x1.shape) - 2)))
        v2  = torch.bmm(v1, self.linear1.weight, self.linear1.bias)

        v3  = x2.permute([0, len(x2.shape)-1] + list(range(len(x2.shape) - 2)))
        v4  = torch.bmm(v3, self.linear2.weight, self.linear2.bias)

        return (v2, v4), v2


# Initializing the model