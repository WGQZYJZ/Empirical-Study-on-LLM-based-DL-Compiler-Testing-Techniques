
class MultiheadAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self.embed_dim = config["hidden_size"] 
        self.key_embed = torch.nn.Linear(
            config['embed_dims'] * config['num_attention_heads'], 
            self.embed_dim)
 
        self.value_embed = torch.nn.Linear(
            config['embed_dims'] * config['num_attention_heads'], 
            self.embed_dim,
        )
 
    def forward(self, key):
        v1  = self.key_embed(key).transpose(-2,-1)
        v3  = self.value_embed(key)
        return v1,v3
 
attn = MultiheadAttention({"hidden_size":4,"embed_dims":8,"num_attention_heads":2})

