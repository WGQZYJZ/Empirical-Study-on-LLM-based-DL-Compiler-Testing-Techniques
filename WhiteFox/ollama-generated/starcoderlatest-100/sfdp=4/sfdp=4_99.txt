
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, 3, 64, 64))
        self.value = torch.nn.Parameter(torch.randn(1, 8, 64, 64))
        self.attn_mask = torch.nn.Parameter(torch.randint(-50, 50, size=(1, 1)))
 
    def forward(self, query, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Inputs to the model
query = torch.randn(3, 64, 64)
value = torch.randn(8, 64, 64)
