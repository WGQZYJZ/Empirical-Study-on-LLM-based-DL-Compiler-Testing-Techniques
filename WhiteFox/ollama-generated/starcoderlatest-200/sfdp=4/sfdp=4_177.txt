
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        query    = self.query(x)
        key      = self.key(x)
        qk       = (query @ key.transpose(-2,-1)) / math.sqrt(query.size(-1))
        attn_mask = torch.cat([torch.eye(attn_dim).unsqueeze(0), -torch.eye(attn_dim).unsqueeze(0)], dim=0)
        qk       = qk + attn_mask
        attn_weight  = torch.softmax(qk, dim=-1)
        output       = (attn_weight @ value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
