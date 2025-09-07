
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk = (v1 @ x1).transpose(-2, -1) / math.sqrt(v1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        v2 = (attn_weight @ x1).transpose(-2, -1)  # Compute the dot product of the dropout output and the value
        return v2


# Initializing the model
m = Model()


