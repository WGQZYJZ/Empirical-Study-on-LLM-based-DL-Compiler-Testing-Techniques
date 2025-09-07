
class AttentionModel(torch.nn.Module):
    def __init__(self, num_heads=128, dropout_p=0.5):
        super().__init__()
 
        self.num_heads = 128
        self.attn = torch.nn.MultiheadAttention(768, 4)
 
        self.dropout = torch.nn.Dropout(0.5)
 
    def forward(self, query, key, value):
        attn_output  = self.attn(query, key, value)[0]
        return attn_output
# Initializing the model
model = AttentionModel()

 # Inputs to the model
query = torch.randn(128, 30, 768)
key   = torch.randn(128, 35, 768)
value = torch.randn(128, 45, 768)

 # Initializing an attention mask with the query.size(-1) length
attn_mask = torch.full((query.size(-1), key.size(-1)), -float('inf'))
 
 # Attention masks for each row in batch: mask out pad tokens (0s) and future tokens (1s).
for i, j in zip(range(35), range(768)):
    attn_mask[j][i] = 1.0

 # Input for the model: the query, key and value, and an attention mask with the query length.
attn_output = model(query=query,key=key,value=value,attn_mask=attn_mask)
 
