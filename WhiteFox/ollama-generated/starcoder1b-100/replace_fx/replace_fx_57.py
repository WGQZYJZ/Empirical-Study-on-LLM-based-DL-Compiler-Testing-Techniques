
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.functional.dropout

    def forward(self, x1):
        v1  = self.dropout(x1)
        return v1

