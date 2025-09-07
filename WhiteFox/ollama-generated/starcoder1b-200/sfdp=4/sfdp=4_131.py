
class Model(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_heads=8, max_len=50, dropout=0.1):
        super().__init__()

        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)
        self.rnn = torch.nn.LSTM(embedding_dim, hidden_dim, num_layers=2, dropout=dropout)

        self.fc = torch.nn.Linear(hidden_dim * 4, vocab_size)

    def forward(self, inputs, inputs_mask):
        # inputs: [batch_size, max_len, embedding_dim]
        # inputs_mask: [batch_size, max_len]
        inputs_shape = list(inputs.shape)
        inputs_shape[0] *= num_heads  # Change batch dimension from "T" to "H"
        shape = [num_heads, -1, hidden_dim // num_heads] + inputs_shape

        x  = self.embedding(inputs).permute(*inputs_shape)  # permute dimensions of the input tensor
        x, _ = self.rnn(x, None)  # forward the sequence through a LSTM
        
        batch_size, max_len = x.shape[0], x.shape[1]  # batch size and sequence length

        x  = torch.flatten(x, start_dim=2).contiguous()
        inputs_seq_len = torch.sum(inputs_mask, dim=-1)
        
        output_layer = self.fc(torch.cat((x, inputs_mask), -1))
        
        # Add the sequence length to the output layer
        seq_len_tensor = torch.full((batch_size, max_len, 1), fill_value=max_len, dtype=torch.long)
        seq_len_tensor[range(batch_size), inputs_mask] = inputs_seq_len
        
        # Get the output from the LSTM layer and add it to the input tensor to construct a new sequence
        y  = torch.cat([output_layer, seq_len_tensor], dim=-1)
        y  = self.fc(y)

        return y


# Initializing the model
m = Model(vocab_size=20000, embedding_dim=512, hidden_dim=256, max_len=max_len, dropout=dropout)


