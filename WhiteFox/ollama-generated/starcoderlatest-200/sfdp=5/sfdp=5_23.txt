
class AttentionMechanism(torch.nn.Module):
    def __init__(self, dim_q, dim_kv, dim_k=None):
        super().__init__()
        self.query = torch.nn.Linear(dim_q, dim_k) if dim_k else torch.nn.Identity() # Initialize the query with linear layer
        self.key   = torch.nn.Linear(dim_kv, dim_k) if dim_k else torch.nn.Identity() # Initialize the key with linear layer
 
    def forward(self, x1):
        q  = self.query(x1)  # Project from feature dimension to embedding dimension and compute dot product
        v  = self.key   (x1)  # Project from feature dimension to embedding dimension and compute dot product
        attn_weight = torch.softmax(q @ v, dim=-1) # Compute softmax over the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout
        output = attn_weight @ v  # Dot product of the attention weight and value to compute output
        return output
 
 class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) # Define convolutional layer
        self.attention = AttentionMechanism(dim_q=1, dim_kv=64) # Initialize attention mechanism

    def forward(self, x):
        v1  = self.conv(x)   # Convolve to feature dimension and apply convolution operation
        attn_out = self.attention(v1)   # Compute attention weights with input tensor `v1`
        output = attn_out + v1    # Add scaled dot product from the attention layer to the original input
        return output


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
