
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.randn(2, 3, 4, 5)
        self.query = torch.randn(1, 8, 2048, 192)
        self.key = torch.randn(1, 8, 2048, 192)
 
    def forward(self, x1):
        qk  = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1))
        qk  = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output  = attn_weight @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
