
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv_key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(2, 3, 64, 64)
