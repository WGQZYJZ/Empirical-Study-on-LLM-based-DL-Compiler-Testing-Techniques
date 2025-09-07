
class Model(torch.nn.Module):
    def __init__(self, hidden_size=256):
        super().__init__()
        self.query = torch.nn.Linear(512, hidden_size)
        self.key = torch.nn.Linear(512, hidden_size)
        self.value = torch.nn.Linear(hidden_size, 1)
 
    def forward(self, x):
        b, c, h, w = x.shape
        qkv = torch.cat([self.query(x[:, :, :, :]).unsqueeze(-2),
                           self.key(x[:, :, :, :]).unsqueeze(-1)], dim=-1)
        attn_weight = torch.softmax(qkv, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        v = torch.matmul(attn_weight, self.value(x))
        return v


# Inputs to the model
x1 = torch.randn(1, 512, 64, 64)
