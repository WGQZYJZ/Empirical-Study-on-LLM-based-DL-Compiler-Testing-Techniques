
class Model(torch.nn.Module):
    def __init__(self, dim_q: int = 30, dim_k: int = 64, dim_v: int = 256):
        super().__init__()
        self.dim_q  = dim_q
        self.dim_k  = dim_k
        self.dim_v  = dim_v
        self.query  = torch.nn.Embedding(vocab_size, dim_q)
        self.key    = torch.nn.Embedding(vocab_size, dim_k)
        self.value  = torch.nn.Embedding(vocab_size, dim_v)
 
    def forward(self, x1, x2):
        # Query: [Batch Size, Time Length] x [Vocab Size, Embedding Dimension] -> [Batch Size, Vocab Size, Embedding Dimension]
        self.query(x1)  # Compute the embedding for x1
        # Key:   [Batch Size, Embedding Dimension] x [Vocab Size, Embedding Dimension] -> [Batch Size, Time Length, Vocab Size, Embedding Dimension]
        self.key(x2)    # Compute the embedding for x2
        # Value: [Batch Size, Time Length, Vocab Size, Embedding Dimension] -> [Batch Size, Time Length, Vocab Size, Embedding Dimension]
        self.value(x1)  # Compute the embedding for x1
        # Query dot Key (batch size, dim_k) -> [Batch Size, Vocab Size]
        query_key = torch.matmul(self.query, self.key.transpose(-2, -1))
        # Scale: [Batch Size, Vocab Size] x [Batch Size, Vocab Size]
        inv_scale = 1 / (self.dim_k ** -0.5)
        # Softmax [Batch Size, Vocab Size] -> [Batch Size, Vocab Size]
        scaled_query_key = query_key * inv_scale  # Apply softmax to the query dot key
        # Dropout [Batch Size, Vocab Size] x (p=dropout_p)
        dropout_qk = torch.nn.functional.dropout(scaled_query_key, p=dropout_p)
        # Dot Product: [Batch Size, Time Length, Vocab Size] -> [Batch Size, Time Length, Vocab Size]
        output = dropout_qk.matmul(self.value)  # Compute the dot product of the dropout qk and value
        return output


# Initializing the model
m  = Model()

# Inputs to the model
x1   = torch.randn(1, 64, dtype=torch.float32, device='cuda')  # (batch size, feature dimension)
x2   = torch.randn(2, 20, dtype=torch.float32, device='cuda')  # (batch size, target dimension)
