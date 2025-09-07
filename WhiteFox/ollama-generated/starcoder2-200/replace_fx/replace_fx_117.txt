
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1, p=0.5)
        v3  = v2 + torch.rand_like(v2).to(device="cuda:0") if not torch.backends.mps.is_available() else v2
        return v3

m = Model()

