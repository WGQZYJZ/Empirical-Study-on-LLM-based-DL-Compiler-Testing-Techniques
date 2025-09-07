
class AttentionModel(torch.nn.Module):
    def __init__(self, attn_mask=None):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 2)
        self.dropout1 = torch.nn.Dropout(0.5)
        self.dropout2 = torch.nn.Dropout(0.3)
 
    def forward(self, query, key):
        v1 = self.attn(query, key)[0]
        v1 = self.dropout1(v1)
        v1 = v1 + query
        return v1
 
 # Initializing the model
m = AttentionModel()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 32, 64, 64)
attn_mask = (x2 != 0).type(torch.float).repeat(1, 2, x2.size(-2), x2.size(-1))
