
class Model(torch.nn.Module):
    def __init__(self, d_model=1024, dropout_p=0.5):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_model)
        self.key = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x):
        query = self.query(x).transpose(-2, -1) # Shape: [batch_size, head_num, length, dim]
        key   = self.key(x).transpose(-2, -1)
        value = self.value(x)
        attn_weight  = torch.softmax(query @ key / math.sqrt(key.size(-1)), dim=-1) # Shape: [batch_size, head_num, length, length]
        attn_weight = self.dropout(attn_weight).transpose(-2, -1) @ value # Shape: [batch_size, head_num, length, dim]
        output       = torch.cat([value, attn_weight], dim=2) # Concatenate the key and attention weights to the value. This makes a multi-head attention with one or more heads on top of each other
        return output
