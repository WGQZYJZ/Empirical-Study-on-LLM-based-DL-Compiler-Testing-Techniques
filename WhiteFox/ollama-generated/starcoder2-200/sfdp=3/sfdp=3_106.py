
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.dropout = torch.nn.Dropout(config["dropout"])
 
    def forward(self, query, key, value):
        scale_factor  = torch.rsqrt(query.shape[-1]) # Get the sqrt of the query tensor's second dimension
        scaled_qk  = query @ key.transpose(-2, -1) * scale_factor # Compute the dot product of the query and key tensors
        
        scaled_qk += -99999 if torch._isinf(scaled_qk).all() else 0 # Replace inf with -99999

        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk, p=config["dropout"]) # Apply dropout to the softmax output
        output  = dropout_qk @ value # Compute the dot product of the dropout output and the value tensor
 
        return output

# Initializing the model
spa  = ScaledDotProductAttention({
    "dropout": 0.1,
})

