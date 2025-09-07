
class Model(torch.nn.Module):
    def __init__(self, embed_dim=128, nhead=8, num_layers=6):
        super().__init__()
        self.embed_dim = embed_dim
        self.nhead = nhead
        self.num_layers = num_layers
        
        self.encoder = torch.nn.TransformerEncoder(
            torch.nn.TransformerEncoderLayer(embed_dim), num_layers
        )
    
    def forward(self, x):
        # Encode the input
        q = x
        k = None
        v = None
    
        for layer in range(self.num_layers):
            if layer == 0:
                # First layer uses no masking and uses a zero-padding to account for batch size
                attn_mask = torch.ones((q.shape[1], q.shape[2]))  # [batch, seq_len, 1]
            else:
                # Use the results of the previous layer as input
                attn_mask = None
    
            # Compute and scale dot products for this block
            if k is not None:
                q, k, v, _ = self.encoder(q, k, v, attn_mask)
            elif v is not None:
                q, k, _, v = self.encoder(q, None, v, attn_mask)
            else:
                # This layer does not use key and value so we just compute them as before
                q, k, v = self.encoder(q, None, v, attn_mask)
    
        return q


# Initializing the model
m = Model()


