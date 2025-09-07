
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=1, embedding_dim=32):
        super().__init__()
        self.layernorm_qk = torch.nn.LayerNorm(embedding_dim) # layer normalization before query and key projections
        self.q_projection = torch.nn.Linear(embedding_dim, embedding_dim, bias=False)
        self.k_projection = torch.nn.Linear(embedding_dim, embedding_dim * num_attention_heads, bias=False)
 
    def forward(self, q, k):
        v = key @ value.transpose(-2, -1)  # Compute the dot product of the query and key tensors
        scale_factor = (key.size(-1) ** -.5) / math.sqrt(v.size(-1))  # Scale the dot product by a factor
        scaled_qk = q @ self.q_projection(self.layernorm_qk(query))  # Project the query to the same dimension as key tensor using weights from q projection
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk @ self.k_projection(self.layernorm_v(value))  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(2, 3, 64, 64)  # query shape (batch_size, num_attention_heads * embedding_dim, seq_length, embeding_dim)
key = torch.randn(2, 3, 64, 64)    # key shape (batch_size, num_attention_heads * embedding_dim, seq_length, embeding_dim)
value = torch.randn(2, 3, 64, 64) # value shape (batch_size, num_attention_heads * embedding_dim, seq_length, embeding_dim)


