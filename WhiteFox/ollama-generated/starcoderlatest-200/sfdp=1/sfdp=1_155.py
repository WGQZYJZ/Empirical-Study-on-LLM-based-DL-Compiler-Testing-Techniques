
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, value)
        softmax_qk = qk / math.sqrt(qk.shape[-1]) # Scale the dot product by the inverse scale factor
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.attention(query, key, value, attn_weights=None)[0]
        return output
 
 