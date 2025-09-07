
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 16)
        self.key = torch.nn.Linear(8, 16)
        self.value = torch.nn.Linear(8, 8)
 
    def forward(self, x1, x2):
        query = self.query(x1).view(-1, 16)
        key = self.key(x2).view(1, -1, 16)
        value = self.value(x2).view(-1, 8)
        attn_weight = torch.softmax(torch.bmm(query, key), dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = torch.bmm(attn_weight, value)
        return output
