
class Attention(torch.nn.Module):
    def __init__(self, in_dim, kdim=None, vdim=None):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(in_channels=in_dim, dim_per_head=128)
 
    def forward(self, q, key, value, attn_mask):
        attn_weight = self.attn(q, key, value)[0]  # Compute the dot product of the query and key, and scale it
        attn_weight = attn_weight + attn_mask # Add the attention mask to the scaled dot product
        output = torch.matmul(attn_weight, value) # Apply a linear transformation (matrix multiplication) of the dropout output and the value
        return output
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention(128)
 
    def forward(self, x, qk_mask, vq_mask, kq_mask):
        attn_output = self.attn(x, x, x, qk_mask) # Compute the output of attention with a scaled dot product as the input
        x = torch.dropout(attn_output + x, p=0.1, training=self._training_) # Dropout and skip-connect the output
        attn_output = self.attn(x, x, x, vq_mask) # Compute the output of attention with a scaled dot product as the input
        x = torch.dropout(attn_output + x, p=0.1, training=self._training_) # Dropout and skip-connect the output
        attn_output = self.attn(x, x, x, kq_mask) # Compute the output of attention with a scaled dot product as the input
        x = torch.dropout(attn_output + x, p=0.1, training=self._training_) # Dropout and skip-connect the output
        return attn_output
 

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(4, 256, 7, 7)
qk_mask = torch.arange((10), dtype=torch.int8).view(2, -1) < 3 # Masks for query and key, size: batch_size x (query + key dimension)
vq_mask = torch.arange((4), dtype=torch.int8).view(-1) < 2 # Masks for value and query, size: (value dimension + query dimension)
kq_mask = torch.arange((40), dtype=torch.int8).view(5, -1) > 7 # Masks for key and query, size: batch_size x (key + query dimension)
