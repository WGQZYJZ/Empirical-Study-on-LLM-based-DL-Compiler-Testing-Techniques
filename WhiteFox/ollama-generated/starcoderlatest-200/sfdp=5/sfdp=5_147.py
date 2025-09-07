
class Model(torch.nn.Module):
    def __init__(self, d_model=1024):
        super().__init__()

        self.d_model = d_model

        # Embedding layer for queries and keys (query and key shape: [batch_size, seq_length, dim])
        self.embedding_queries  = torch.nn.Embedding(num_embeddings=1000, embedding_dim=self.d_model)
        self.embedding_keys    = torch.nn.Embedding(num_embeddings=1000, embedding_dim=self.d_model)
        
        # Linear layer for the attention weights (attn_weight shape: [batch_size, seq_length, dim])
        self.linear_attn  = torch.nn.Linear(in_features=self.d_model, out_features=1)

    def forward(self, x):

        # Convert inputs to tensors and apply word-level embeddings
        xq  = self.embedding_queries(x[:, :,-3:-1])   # Query shape: [batch_size, seq_length, dim] -> [batch_size, seq_length, d_model]
        xk  = self.embedding_keys(x[:, :,2:])       # Key shape: [batch_size, seq_length, dim] -> [batch_size, seq_length, d_model]

        # Compute the dot product of the query and key (scaled by square root of dimension)
        qk  = xq @ xk.transpose(-1,-2) / math.sqrt(qk.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        
        # Apply dropout to attention weights
        attn_weight = torch.dropout(attn_weight, p=0.3, training=self.training)

        # Output is the dot product of the attention weights and values (scaled by square root of dimension)
        output = attn_weight @ x[:, :,:-2] / math.sqrt(x.size(-1))
        
        return output

    def load_state_dict(self, state_dict):
        