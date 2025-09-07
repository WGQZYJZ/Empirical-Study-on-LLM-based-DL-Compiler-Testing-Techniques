
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_query = torch.nn.Linear(768, 256)
        self.attn_key   = torch.nn.Linear(768, 256)
        self.attn_value = torch.nn.Linear(768, 256)
 
    def forward(self, x1):
        query = self.attn_query(x1)
        key   = self.attn_key(x1)
        value = self.attn_value(x1)

        qk     = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk     = qk + attn_mask
        attn   = torch.softmax(qk, dim=-1)
        output = attn @ value

        return output
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
