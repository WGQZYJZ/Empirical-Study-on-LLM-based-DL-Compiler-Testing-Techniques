
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.dropout(x1, 0.5)
        v3  = torch.nn.functional.rand_like(v2, 4.) # Replace torch.nn.functional.rand_like with torch.nn.functional.lowmem_dropout to simulate this behavior (fallback)
        return v2


# Initializing the model