
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.Linear(128, 64)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk + self.attn_mask, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()
# Inputs to the model
query  = torch.randn(128, 32, 64)
key  = torch.randn(64, 128, 64)
value = torch.randn(128, 32, 64)
