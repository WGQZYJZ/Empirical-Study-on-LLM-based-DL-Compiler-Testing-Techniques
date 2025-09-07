
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 16, 1)
        self.key   = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x1, x2):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk + attn_mask, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()


