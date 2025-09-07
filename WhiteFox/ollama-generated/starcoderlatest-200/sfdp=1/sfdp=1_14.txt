
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(16, 8)
 
    def forward(self, xq, xk, xv):
        v1, attn  = self.attention_layer(xq, xk, xv) # Apply Multi-Head Attention
        scaled_qk = attn / math.sqrt(attn.shape[-1]) # Scale the attention by its square root
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply Softmax to scaled attention
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.25) # Apply Dropout with probability 0.25 on the softmax output
        output = dropout_qk.matmul(xv) # Compute the dot product of the dropout output and value tensor
        return output
# Inputs to the model
xq = torch.randn(16, 16, 128) # Input for key, query, and values
xk = torch.randn(16, 32,  64) # Input for keys
xv = torch.randn(16, 8,   16) # Input for values
