
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(2, 3)
        self.key = torch.randn(5, 4)
        self.attn_mask = torch.tensor([[0., 0., 0.], [1., 0., 0.], [1., 1., 0.], [1., 1., 1.]])
        self.value = torch.randn(3, 7)
 
    def forward(self):
        query_key_dot = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1)) + self.attn_mask
        attn_weights = torch.softmax(query_key_dot, dim=-1) 
        attn_weights  = torch.dropout(attn_weights ,0.5, True )
        attn_out = attn_weights @ value

