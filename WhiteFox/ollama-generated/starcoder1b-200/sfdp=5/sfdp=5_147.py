
class Model(torch.nn.Module):
    def __init__(self, dim_key):
        super().__init__()
        self.dim_key = dim_key

    def forward(self, query, key, attn_mask):
        