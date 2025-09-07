
class Model(torch.nn.Module):
    def __init__(self, attn_dropout=0.1):
        super().__init__()
        self.attn = torch.nn.Linear(768, 32)
        self.attn_dropout = torch.nn.Dropout(attn_dropout)
 
    def forward(self, x1, x2):
        qk  = torch.mm(x1, x2.t()) / math.sqrt(x1.size(-1))
        k   = torch.softmax(qk, dim=-1)
        v   = self.attn(x1).unsqueeze(-1).bmm(k)
        output = torch.nn.functional.dropout(v, p=self.attn_dropout)
        return output


# Initializing the model
m  = Model()

