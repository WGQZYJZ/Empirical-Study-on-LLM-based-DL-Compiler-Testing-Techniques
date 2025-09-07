
class Model(torch.nn.Module):
    def __init__(self, num_layers=3, depth=16, heads=8, d_model=512, nhead=8):
        super().__init__()
 
        self.transformer = torch.nn.Transformer(
            num_layers=num_layers, 
            depth=depth, 
            heads=heads, 
            d_model=d_model,
            nhead=nhead)
 
    def forward(self, x1, x2):
        bsz, seq_len, dim = x1.size()
        attn_mask = torch.zeros(attn_key.shape[0], seq_len, seq_len).to(device)  # Build the attention mask for this batch and sequence

        # Add the attention mask to all dimensions except the time dimension
        attn_mask = add_attention_mask(attn_mask, x1, x2) 
        
        # Use the model to compute attention weights
        qk, _ = self.transformer(x1, x2, key_padding_mask=attn_mask)
        
        # Compute the weighted average of the dropout output and the value, then scale it by sqrt(d_model).
        result = torch.sum((qk * attn_weight), dim=-1) / math.sqrt(self.transformer.d_model)

        return result


# Initializing the model
m  = Model()


