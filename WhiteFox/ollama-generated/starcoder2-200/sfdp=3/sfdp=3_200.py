class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, scale=None, dropout=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout)
        # If no scaling factor is provided, then divide by the square root of the hidden size
        if not scale:
            scale  = torch.rsqrt(torch.tensor([self._scale]))[0]
        self.scale = scale
 
    def forward(self, query, key, value):
        # Compute the dot product between the query and key tensors
        scaled_attn  = torch.matmul(query, key.transpose(-2, -1)) / self.scale
 
        # Apply softmax to each row of the dot product
        softmax_attn  = scaled_attn.softmax(dim=-1)
 
        
        # Dropout is applied to the output of the attention
        dropout_attn  = self.dropout(softmax_attn)
 
        

        return torch.matmul(dropout_attn, value)
