
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim_key: int, num_heads: int, dropout_p: float = 0):
        super().__init__()
        self.num_heads = num_heads
        self.dropout_p = dropout_p
 
        # Embedding layer to embed the keys and values in an all-dimensional feature vector
        self.key_layer = torch.nn.Linear(dim_key, dim_key)
        self.value_layer = torch.nn.Linear(dim_key, dim_key)
 
        # Fully connected layer to compute scaled dot product between query and key for computing attention weights
        self.scale = torch.sqrt(torch.tensor(2.0 / (num_heads + 1)))
        self.query_layer = torch.nn.Linear(dim_key, num_heads * dim_key)
 
    # This layer computes the scaled dot product between query and key, then applies softmax to get attention weights
    def forward(self, x):
        # Embedding of the input tensor into a 2-dimensional vector with shape [1, max_query_len, dim_model]
        q = self.query_layer(x)
        # Shape: [batch_size, max_query_len, num_heads, dim_key], where max_query_len is the length of the query sequence (in tokens).
        q = torch.reshape(q, shape=(q.shape[0], q.shape[1], self.num_heads, q.shape[-1]))
 
        # Embedding of the keys into a 2-dimensional vector with shape [1, max_key_len, dim_model]
        k = self.key_layer(x)
        # Shape: [batch_size, max_key_len, num_heads, dim_key], where max_query_len is the length of the key sequence (in tokens).
        k = torch.reshape(k, shape=(k.shape[0], k.shape[1], self.num_heads, k.shape[-1]))
 
        # Embedding of the values into a 2-dimensional vector with shape [1, max_key_len, dim_model]
        v = self.value_layer(x)
        # Shape: [batch_size, max_key_len, num_heads, dim_key], where max_query_len is the length of the value sequence (in tokens).
        v = torch.reshape(v, shape=(v.shape[0], v.shape[1], self.num_heads, v.shape[-1]))
 
        # Apply scaled dot product between query and key to get attention weights
        attn_score = torch.matmul(q, k.transpose(-2, -1)) * self.scale
        attn_score += torch.tensor([-20000.0])  # Add a constant for numerical stability.
 
        # Get the softmax of scaled dot product to get attention weights
        attn_weight = torch.softmax(attn_score, dim=-1)
        attn_weight = torch.dropout(attn_weight, self.dropout_p, True)
 
        # Compute the output with attention applied on top of value vector (x). Shape: [batch_size, max_query_len, num_heads * dim_value]
        output = torch.matmul(attn_weight, v)
 
        return output  # The shape of output is [1, max_query_len, num_heads * dim_value].


# Initializing the model
m = MultiHeadAttention(dim_key=3, num_heads=2, dropout_p=0.5)
 
 # Inputs to the model
  x = torch.randn(1, 3, 64, 64) 
  