
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, 8, 64, 64))
        self.key = torch.nn.Parameter(torch.randn(1, 8, 64, 64))
        self.value = torch.nn.Parameter(torch.randn(1, 8, 64, 64))
 
    def forward(self, query, key):
        # Scale the dot product by sqrt of dimensionality for softmax calculation
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 8, 64, 64)
key = torch.randn(1, 8, 64, 64)
attn_mask = torch.rand((1, 8, 64, 64))
