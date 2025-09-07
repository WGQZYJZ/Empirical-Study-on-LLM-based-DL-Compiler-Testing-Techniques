
class Model(torch.nn.Module):
    def __init__(self, num_layers=2, seq_length=1024):
        super().__init__()

        # Layer norm
        self.layernorm = torch.nn.LayerNorm(seq_length)

        # Embedding layer (same embedding size as TransformerModel.embedding in TransformerModel.py of this project)
        self.position  = torch.nn.Embedding(1024, seq_length)

        self.layers   = torch.nn.ModuleList()
        for _ in range(num_layers):
            self.layers.append(TransformerLayer())
    
    def forward(self, x1, attn_mask=None):
        # Positional encoding (learnable parameters). The length of positional embedding layer is fixed to 1024. 
        x = self.position(x1)

        # Layer norm + Multi-head attention
        for layer in self.layers:
            x = layer(x, attn_mask=attn_mask)
        return self.layernorm(x).transpose(-1,-2),

# Initializing the model 
m  = Model()


# Inputs to the model
x1 = torch.randint(0, 5, (384,)) 

__output__, __attn_weight__ = m(x1) # Attention weights

