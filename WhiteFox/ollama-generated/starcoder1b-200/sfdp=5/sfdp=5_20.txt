
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dropout = nn.Dropout()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk = x1 @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = self.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        value = x1 @ attn_weight
        return value


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
