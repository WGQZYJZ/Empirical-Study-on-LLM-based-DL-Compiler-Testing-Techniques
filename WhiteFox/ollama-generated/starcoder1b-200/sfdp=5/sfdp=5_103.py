
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(8, 2)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = torch.matmul(attn_weight, x1)
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
