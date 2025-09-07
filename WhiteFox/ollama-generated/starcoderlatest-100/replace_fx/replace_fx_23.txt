
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1, requires_grad=True)
        v2 = torch.nn.functional.dropout(v1, p=0.5, inplace=False)
        v3 = self.linear(v2)
        return v3


# Input to the model
input = torch.randn(1, 2, 4)
