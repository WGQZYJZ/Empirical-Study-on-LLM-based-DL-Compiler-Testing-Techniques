
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim_model, num_heads, dropout=0.1):
        super().__init__()
 
        self.dim_model = dim_model
        self.num_heads = num_heads
        self.dropout = nn.Dropout(p=dropout)
        
        # Define the different heads of multi-head attention
        self.head_q = nn.Linear(self.dim_model, self.dim_model, bias=False)
        self.head_k = nn.Linear(self.dim_model, self.dim_model, bias=False)
        self.head_v = nn.Linear(self.dim_model, self.dim_model, bias=False)
        
    def forward(self, query, key, value):
        # Shape: batch x heads x q_len x dim
        qk  = torch.matmul(query, self.head_q(query))
        # Shape: batch x heads x k_len x dim
        qk += torch.matmul(key, self.head_k(key))
 
        qk = self.dropout(qk)
 
        # Shape: batch x heads x q_len x dim
        softmax_qk  = softmax(qk, dim=-1)
        # Shape: batch x heads x q_len x dim
        output      = torch.matmul(softmax_qk, self.head_v(value))
 
        return output
 
class Transformer(torch.nn.Module):
    def __init__(self, input_dim, num_heads, embedding_size, num_hidden_layers, num_classes):
        super().__init__()

        # Input dim and hidden dim must match, in case of bidirectional LSTM or GRU: the hidden size
        self.embedding = nn.Embedding(input_dim, embedding_size)

        self.num_heads = num_heads
        self.transformer_encoder = torch.nn.ModuleList([
            MultiHeadAttention(self.embedding_size * 2, self.num_heads)
            for _ in range(self.num_hidden_layers)
        ])

    def forward(self, x):
        # Shape: batch x seq_len
        embedding       = self.embedding(x)
 
        x               = torch.transpose(embedding, -1, 2)
        x               = torch.nn.utils.rnn.pack_padded_sequence(
            input=x, lengths=[x.shape[0]] * embedding.shape[0], batch_first=True)

        for module in self.transformer_encoder:
            # Shape: batch x seq_len x dim * 2
            output = module(embedding, embedding, embedding)
            # Shape: batch x seq_len x dim
            _, x       = torch.nn.utils.rnn.pad_packed_sequence(output, batch_first=True)

        output = self.dropout(x)

        return self.fc(output)
