
class Model(torch.nn.Module):
    def __init__(self, dim=512, heads=8):
        super().__init__()
        self.dim = dim
        self.heads = heads
 
        self.attention_layer = torch.nn.MultiheadAttention(dim=dim, num_heads=heads)
 
    def forward(self, query, key, value):
        # Compute the dot product of the query and key tensors
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        
        # Scale the dot product by a factor
        scaled_qk = qk.mul(scale_factor) 
        
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)
        
        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        v = self.attention_layer(query, key, value, attention_mask=dropout_qk)[0]
        return v
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(batch_size, 32, dim=512)
