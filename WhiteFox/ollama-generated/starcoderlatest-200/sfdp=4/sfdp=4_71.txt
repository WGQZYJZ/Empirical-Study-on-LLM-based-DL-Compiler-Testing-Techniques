
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.ones((1, 128, 10, 10))
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk + self.attn_mask, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(256, 3, 128, 64)
k = torch.randn(256, 8, 128, 64)
v = torch.randn(256, 8, 10, 10)
