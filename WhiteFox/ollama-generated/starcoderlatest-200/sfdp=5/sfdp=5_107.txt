
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)
 
    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose(-1,-2)) / math.sqrt(x1.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value
        return output


# Input to the model
x1 = torch.randn(1, 8)  # [batch_size=1]
x2 = torch.randn(1, 16)  # [batch_size=1]
x3 = torch.randn(1, 10)  # [batch_size=1]
