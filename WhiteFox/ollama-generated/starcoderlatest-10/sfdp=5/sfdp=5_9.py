
class Model(torch.nn.Module):
    def __init__(self, nhead = 4, attn_dropout=0.1):
        super().__init__()
        self.nhead = nhead
        self.attn_fc1 = torch.nn.Linear(768*3, 768)
        self.attn_drop = torch.nn.Dropout2d(attn_dropout)
        self.attn_fc2 = torch.nn.Linear(768, 256)
        self.attn_norm = torch.nn.LayerNorm(768*3)
 
        self.value_fc1 = torch.nn.Linear(768*3, 768)
        self.value_drop = torch.nn.Dropout2d(attn_dropout)
        self.value_fc2 = torch.nn.Linear(768, 256)
        self.value_norm = torch.nn.LayerNorm(768*3)
 
        self.key_fc1 = torch.nn.Linear(768*3, 768)
        self.key_drop = torch.nn.Dropout2d(attn_dropout)
        self.key_fc2 = torch.nn.Linear(768, 256)
        self.key_norm = torch.nn.LayerNorm(768*3)
 
    def forward(self, qk1):
        q, k, v = qk1
        v  = self.value_fc1(torch.cat([v, k], dim=1)) * math.sqrt(2/v.size(-1))
        v = v + self.value_norm(v)
        v = F.gelu(self.value_drop(self.value_fc2(v)))
 
        k = self.key_fc1(torch.cat([k, v], dim=1)) * math.sqrt(2/k.size(-1))
        k = k + self.key_norm(k)
        k = F.gelu(self.key_drop(self.key_fc2(k)))
 
        attn_weight  = torch.softmax(qk, dim=-1) * math.sqrt(v.size(-1)) 
        attn_weight = torch.dropout(attn_weight, self.attn_dropout, True)
        output = attn_weight @ v
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
qk1 = (torch.randn(1024, 3, 128, 128), 
        torch.randn(1024, 3, 128, 128),
        torch.randn(1024, 768*3, 56, 56))
