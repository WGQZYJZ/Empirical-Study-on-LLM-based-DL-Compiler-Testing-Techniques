
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads=8, query_dim=128, key_dim=128, value_dim=128, dropout_p=.1):
        super().__init__()
 
        self.num_heads = num_heads
        self.query_dim  = query_dim
        self.key_dim    = key_dim
        self.value_dim  = value_dim
 
        # Create the multi-head attention layers
        self.w_qs = torch.nn.Linear(self.query_dim,  self.num_heads * self.query_dim)
        self.w_ks = torch.nn.Linear(self.key_dim,    self.num_heads * self.key_dim)
        self.w_vs = torch.nn.Linear(self.value_dim,  self.num_heads * self.value_dim)
 
        # Create the output projection layer and dropout layers
        self.out_proj = torch.nn.Sequential(
            torch.nn.Dropout2d(p=dropout_p),
            torch.nn.Conv2d(self.num_heads * self.value_dim, value_dim, kernel_size=(1, 1)),
        )
 
    def forward(self, query, key, value):
 
        # Reshape the tensors so that the dot product function can be computed easily
        bs, num_heads, _, _ = query.shape 
        q = self.w_qs(query).view(bs, -1, self.num_heads, self.query_dim)
        k = self.w_ks(key).view(bs, -1, self.num_heads, self.key_dim)
        v = self.w_vs(value).view(bs, -1, self.num_heads, self.value_dim)
 
        # Compute the dot product of q with k and multiply it by a scaling factor to get scaled_qk
        dots = torch.matmul(q, k.transpose(-2,-1)) 
        dots *= (1 / math.sqrt(self.key_dim))

        attn = self._scaled_attention(dots) # Apply the dot product to create attention weights using an implementation detail of the library
        attn = attn.view(bs, -1, num_heads * self.value_dim)
        attn = self._dropout(attn)
 
        output = self.out_proj(attn)

        return output
 
    def _scaled_attention(self, dots): # Implementation detail of the library
        attn = torch.softmax(dots, dim=-1) 
        return attn

    def _dropout(self, x):
        return torch.nn.functional.dropout2d(x, p=0.5)

class Model(torch.nn.Module):
    def __init__(self, num_heads=8, query_dim=128, key_dim=128, value_dim=128, dropout_p=.1):
        super().__init__()
 
        # Create the multi-head attention layers
        self.multi_head_attention = MultiHeadAttention(num_heads, query_dim, key_dim, value_dim, dropout_p)
 
    def forward(self, query, key, value):
 
        output = self.multi_head_attention(query, key, value)

        return output
# Initializing the model and input tensors for the model example
m = Model()
q = torch.randn(1, 3, 64, 64) # shape=(batchsize=1, channel=3, H=64, W=64)
k = torch.randn(1, 3, 64, 64) # shape=(batchsize=1, channel=3, H=64, W=64)
v = torch.randn(1, 3, 64, 64) # shape=(batchsize=1, channel=3, H=64, W=64)


# Generating the output tensor for the model example
output = m(q, k, v)


