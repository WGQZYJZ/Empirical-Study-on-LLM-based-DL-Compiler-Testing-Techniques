
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = torch.nn.Conv2d(3, 16, 1)
        self.key_layer = torch.nn.Conv2d(3, 16, 1)

    def forward(self, x1):
        qk = (self.query_layer @ x1 + self.key_layer @ x1).transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
