
class Model(torch.nn.Module):
    def __init__(self, attn_dropout=0., layerdrop_p=0.1, heads=8):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=3, num_heads=heads)
 
    def forward(self, x1, x2):
        batch_size, q_len, v_len, embed_dim = 1, 64, 64, 3
        query = torch.rand(batch_size, q_len, embed_dim).to(x1.device)
        key = torch.rand(batch_size, k_len, embed_dim).to(x1.device)
        value = torch.rand(batch_size, v_len, embed_dim).to(x1.device)
 
        attn_weights = self.attn(query=query, key=key, value=value)[0]
 
        return (attn_weights)
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 64, 64).to("cpu")
x2 = torch.randn(32, 64, 64).to("cpu")
