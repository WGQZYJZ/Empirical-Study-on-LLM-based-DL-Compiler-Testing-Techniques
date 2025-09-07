
class SelfAttentionLayer(torch.nn.Module):
    def __init__(self, d_model, h=8):
        super().__init__()
        
        self.q = torch.nn.Linear(d_model, d_model) # Compute the dot product of the query and key (plus an attention mask), followed by a dropout operation
        self.k = torch.nn.Linear(d_model, d_model)
        self.v = torch.nn.Linear(d_model, d_model)
 
        self._attn = torch.nn.MultiheadAttention(h=8)
        self.dropout1 = torch.nn.Dropout(.5)
 
    def forward(self):
        x  = self._attn(x1, x2)[0]
