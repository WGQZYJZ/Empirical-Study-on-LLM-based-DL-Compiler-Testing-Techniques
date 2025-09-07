
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout  = torch.nn.Dropout(...)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, self.dropout.p)
        v2 = torch.rand_like(input_tensor, ...)
        return v2


