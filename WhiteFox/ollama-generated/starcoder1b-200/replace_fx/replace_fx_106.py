
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor
        v2 = torch.rand_like(x1, requires_grad=True)
        return v2


