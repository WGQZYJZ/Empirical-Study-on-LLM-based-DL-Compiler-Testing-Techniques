
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(32, 8, 64, 64)
key    = torch.randn(32, 16, 64, 64)
value  = torch.randn(32, 80, 64, 64)
attn_mask = torch.arange(query.size(-1)).reshape((1,-1,1,1)) != attn_mask # This is an attention mask which indicates that the position of the attention should be set to 0 when computing the dot product with a key tensor
