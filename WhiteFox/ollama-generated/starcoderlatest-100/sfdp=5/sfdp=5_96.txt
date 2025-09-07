
class Model(torch.nn.Module):
    def __init__(self, num_heads, d_model):
        super().__init__()
        self.num_heads = num_heads
        self.d_model = d_model
 
        self.query = torch.nn.Linear(d_model, d_model)
        self.key = torch.nn.Linear(d_model, d_model)
 
    def forward(self, x):
        batch_size = x.shape[0]
        seq_len = x.shape[-1]
 
        query = self.query(x).view(batch_size, -1, self.num_heads, 
                               self.d_model // (self.num_heads * self.d_model)).transpose(-2, -1) 
        key = self.key(x).view(batch_size, -1, self.num_heads, 
           self.d_model // (self.num_heads * self.d_model)).transpose(-2, -1)
 
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) 
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value.view(batch_size, seq_len, self.d_model)
 
        return output


# Initializing the model
m = Model(8, 512)


# Inputs to the model
x = torch.randn(64, 8, 512)
