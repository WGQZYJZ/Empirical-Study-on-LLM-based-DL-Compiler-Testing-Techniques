
class SelfAttention(torch.nn.Module):
    def __init__(self, d_model=768, dropout=0.1, max_seq_length=512):
        super().__init__()
        self.d_model  = d_model
        self.dropout  = torch.nn.Dropout(p=dropout)
        self.query   = torch.nn.Linear(in_features=self.d_model, out_features=self.d_model)
        self.key    = torch.nn.Linear(in_features=self.d_model, out_features=self.d_model)
        self.value  = torch.nn.Linear(in_features=self.d_model, out_features=self.d_model)
 
    def forward(self, x1):
        v20  = self.query(x1).transpose(-2, -1)
        v30  = math.sqrt(v20.size(-1)) 
        v40  = torch.div(v20, 512 ** 0.5)
        v70  = self.key(x1).transpose(-2, -1)  
        v80  = math.sqrt(v70.size(-1))
        v90  = torch.div(v70, 512 ** 0.5)
        v130 = v40 @ v90 
        v140 = self.dropout(self.attn_mask(v80, v20))
        v160 = torch.add(v130, v140)
        v170 = torch.softmax(v160, dim=-1) # Apply softmax to the result
        v290  = self.value(x1).transpose(-2, -1) 
        v380  = v170 @ v290
        return v380

# Initializing the model
m  = SelfAttention()

