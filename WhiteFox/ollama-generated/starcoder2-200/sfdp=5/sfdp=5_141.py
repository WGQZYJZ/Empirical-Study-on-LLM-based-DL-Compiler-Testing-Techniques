
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self._attn = torch.nn.MultiheadAttention(
            embed_dim=config["embed_dim"], 
            num_heads=4)

    def forward(self, query, key, value):
        attn_weight  = self._attn(query, key, value)[0] 
        output = (attn_weight @ value).unsqueeze(-1)
        return output

# Initializing the model
m = Model({
  "embed_dim":256
})

 # Inputs to the model
 query = torch.randn(4, 8, 256)
 key   = torch.randn(4, 8, 256) 
 value = torch.randn(4, 1024, 256) 
 __output__  = m(query, key, value).squeeze(-1)

