
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, query_dim, key_dim, value_dim):
        super().__init__()

        # Initialize the linear layers for scaled dot product attention module
        self.scaled_q = torch.nn.Linear(query_dim, key_dim)
        self.scaled_k = torch.nn.Linear(key_dim, query_dim)
        self.scaled_v = torch.nn.Linear(value_dim, query_dim)

    def forward(self, x1, x2):
        # Linear transformation of queries to keys, attention weights and values for the scaled dot product mechanism
        # The shape of key, query, value is batch-size x num_heads x seq_length x dim per head.

        q = torch.tanh(self.scaled_q(x1))
        k = torch.tanh(self.scaled_k(x2))
        v = torch.tanh(self.scaled_v(x2))

        # Compute attention weights of shape batch-size x num_heads x seq_length x dim per head
        scaled_dot_product  = torch.matmul(q, k.transpose(-2,-1)) / math.sqrt(key_dim)
        attention_weights = scaled_dot_product.softmax(dim=-1)

        # Compute a weighted sum of the value tensor by taking the dot product of attention weights and values.
        # The shape of output is batch-size x num_heads x seq_length x dim per head.
        output = torch.matmul(attention_weights, v)
        return output


# Initializing the model
m = ScaledDotProductAttention(query_dim=128, key_dim=128, value_dim=512)
