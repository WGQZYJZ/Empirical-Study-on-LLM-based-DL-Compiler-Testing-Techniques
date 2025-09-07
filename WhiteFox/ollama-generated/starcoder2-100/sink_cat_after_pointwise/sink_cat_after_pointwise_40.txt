
class Model(torch.nn.Module):
    def __init__(self,  dim1=32):
        super().__init__()

        self.linear = torch.nn.Linear(dim1**4 + dim1**5,  dim1)

    def forward(self, x0):
        v2 = [x for i in range(len(x0))] # list comprehension
        v2 = torch.stack([v3 for v3 in v2], 1).view(-1)

        return self.linear(v2),

# Initializing the model