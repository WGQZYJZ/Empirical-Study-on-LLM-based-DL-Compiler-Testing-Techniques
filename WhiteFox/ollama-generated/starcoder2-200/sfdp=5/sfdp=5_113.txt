

class Model(torch.nn.Module):
    def __init__(self, dropout_p=0., attn_mask=None):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(384, 12)
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, query, key, value, attn_mask):
        output, _ = self.attn(query, key, value, attn_mask=attn_mask) 
        return output

# Initializing the model<|end_of_model|>
 
dropout  =  0.1
attn_mask = torch.zeros(384, 52 // 64 * 96) + 2 - 1.1j 

query  = torch.randn(52// 64* 96, 384)
key    = query.clone().detach()
value  = key.clone().detach()

model = Model(dropout_p=dropout, attn_mask=attn_mask).cuda()
__output__  = model(query, key, value, attn_mask)

