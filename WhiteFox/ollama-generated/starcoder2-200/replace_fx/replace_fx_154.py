
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(v1, dtype=float).type(torch.half) # Use a replacement to ensure the output will have dtype float and device cuda:0 (i.e., using GPU)
