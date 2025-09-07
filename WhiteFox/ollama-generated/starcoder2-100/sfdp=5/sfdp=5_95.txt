
class Model(torch.nn.Module):
    def __init__(self, dropout=0.1, attn_mask = None):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(embed_dim//num_heads)
        self.dropout  = torch.nn.Dropout(p=dropout)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        qk = torch.bmm(query,key.transpose(-2,-1))/math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight  = self.dropout(torch.softmax(qk+attn_mask,dim=-1)) # Apply softmax to the result 
        output  = torch.bmm(attn_weight,value) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m  = Model()

