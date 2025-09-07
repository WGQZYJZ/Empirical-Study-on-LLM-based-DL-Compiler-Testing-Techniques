
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 256)
        self.key   = torch.nn.Linear(512, 256)
        self.value = torch.nn.Linear(512, 256)
 
    def forward(self, query, key):
        v1 = self.query(query).unsqueeze(dim=-1)
        v2 = self.key(key).unsqueeze(dim=0)
        v3 = self.value(v1 + v2)
        return v3
 
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = Attention()
 
    def forward(self, x1, x2):
        attention_output = self.attention(x1, x2)
        return attention_output
 
