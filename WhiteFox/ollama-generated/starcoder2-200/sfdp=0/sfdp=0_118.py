
class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # These will be used to compute the scaled dot product attention
        self.norm1  = torch.nn.LayerNorm(d_model)
        self.dropout1  = torch.nn.Dropout(dropout)

        self.norm2  = torch.nn.LayerNorm(d_model)
        self.dropout2  = torch.nn.Dropout(dropout)

    def forward(self, qkv):
        residual  = qkv
        # Apply the scaling normalization layer and dropout
        normalized1  = self.norm1(qkv)

        # Compute scaled dot product attention using the weights, value tensor 
        # from the encoder and the key/query tensors from the decoder
        weights = torch.matmul(normalized1, key.transpose(-2, -1)) / inv_scale
        attention_weights  = weights.softmax(dim=-1)

        # Apply dropout to the output of scaled dot product attention
        out = self.dropout1(self.norm2(qkv  * attention_weights + residual))

        return out

