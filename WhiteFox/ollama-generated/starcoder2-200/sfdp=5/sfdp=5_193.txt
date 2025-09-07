
class Model(torch.nn.Module):
    def __init__(self, query_size, key_size, dropout=0.1):
        super().__init__()

        self.dropout = torch.nn.Dropout(p=dropout)
        self.softmax  = torch.nn.Softmax(-1)
        self.attn  = torch.nn.Linear(query_size + key_size, query_size * 2).float()
 
    def forward(self, x):

        v0 = self.attn(x) 
        query = v0[:, :-key_size]
        key   = v0[:, -key_size:]
 
        v1 = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.shape[-1])
        v2 = self.softmax(v1 + attn_mask)

        v3  = self.dropout(v2)
        v4  = torch.einsum("abcde,e->abcd", v0, v3).contiguous()

        return v4


# Initializing the model