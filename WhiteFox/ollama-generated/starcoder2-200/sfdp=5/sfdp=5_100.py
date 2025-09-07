
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(64, 8)
 
    def forward(self, query, key, value, mask=None, dropout_p=0.5):
        if mask is not None:
            mask = mask[:, None] > math.sqrt(torch.finfo(query.dtype).eps)  # Apply the sqrt operation to the threshold of float precision
        attn_output = self.attn(query, key, value)[0] + query  # Add the scaled query and attention output back together
        return torch.dropout(attn_output, dropout_p, True), attn_weight


# Initializing the model