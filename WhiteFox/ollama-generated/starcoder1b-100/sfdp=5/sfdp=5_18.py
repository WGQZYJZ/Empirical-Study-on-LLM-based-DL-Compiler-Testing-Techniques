
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, mask=None):
        v1 = self.conv(x1)
        # ...
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        # ...
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        # ...
        return attn_weight @ value


# Initializing the model
m = Model()


