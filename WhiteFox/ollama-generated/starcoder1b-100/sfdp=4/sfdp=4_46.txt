
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 32)
        self.key   = torch.nn.Linear(768, 32)
        self.value = torch.nn.Linear(32, 768)

    def forward(self, x1):
        qk = torch.einsum('bij, bij->bi', x1, self.query)
        key = self.key(x1).transpose(-2, -1)
        attn_mask = torch.sparse_max(torch.mm(qk, key), 0) # Use max in the square root of the dot product to avoid divide by zero
        attn_weight = torch.softmax(qk / math.sqrt(key.size(-1)), dim=-1)
        value   = self.value(x1)
        output  = attn_weight @ value + attn_mask
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
