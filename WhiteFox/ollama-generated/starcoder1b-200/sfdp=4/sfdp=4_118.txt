
class Model(torch.nn.Module):
    def __init__(self, attention_dropout: float = 0.1):
        super().__init__()
        self.attention_dropout = nn.Dropout(attention_dropout)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        v = torch.matmul(attn_weight, x2)
        output = v + self.attention_dropout(v)

# Initializing the model
m = Model()

