
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_fc1 = torch.nn.Linear(128, 64) 
        self.attn_fc2 = torch.nn.Linear(64, 32)
        self.attn_fc3 = torch.nn.Linear(32, 16)
        self.attn_fc4 = torch.nn.Linear(16, 8)
 
    def forward(self, x1, key): 
        k = self.attn_fc1(key)
        q = self.attn_fc2(x1)
        v = self.attn_fc3(x1)
        d = self.attn_fc4(torch.cat([k, q, v], dim=1))
 
        attn_weight  = torch.softmax(d, dim=-1) # Apply softmax to the result
        attn_weight  = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        return (attn_weight * v).sum(dim=1)
 
    def attention_fc(self, key):
        k = self.attn_fc1(key)
        q = self.attn_fc2(x1)
        v = self.attn_fc3(x1)
        d = self.attn_fc4(torch.cat([k, q, v], dim=1))
 
        attn_weight  = torch.softmax(d, dim=-1) # Apply softmax to the result
        return (attn_weight * v).sum(dim=1)
 
    def attention_fc2(self, query, key): 
        k = self.attn_fc1(key)
        q = self.attn_fc2(query)
        attn_weight  = torch.softmax((k @ q), dim=-1) # Apply softmax to the result
        return (attn_weight * v).sum(dim=1)
