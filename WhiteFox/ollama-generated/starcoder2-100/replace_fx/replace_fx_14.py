
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.dropout(x1), torch.rand_like(x1)  # dropout is replaced with lowmem_dropout in graph

