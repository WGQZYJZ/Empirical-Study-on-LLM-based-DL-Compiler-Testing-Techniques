class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(v1, 1.3) # The initial value of v2 is set to be the result of multiplying 1.3 and 1/2
        return v2
