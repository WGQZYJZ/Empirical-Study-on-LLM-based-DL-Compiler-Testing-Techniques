
class Model(torch.nn.Module):
    def __init__(self, d_model, heads, dim_feedforward, pffn_num_layers=4, dropout_p=0.2):
        super().__init__()
        self.dim_feedforward = dim_feedforward  # The size of the input embedding (usually equal to `d_model`)
        self.heads = heads  # Number of attention heads
        self.scale = torch.sqrt(torch.FloatTensor([d_model])).unsqueeze(-1)
        self.head_dim = int(d_model / heads)
        self.num_layers = pffn_num_layers  # The number of PFFN layers in the model
        self.attention = torch.nn.MultiheadAttention(self.heads, dim_feedforward, dropout=dropout_p)
        self.positionwise_feedforward = PositionWiseFeedForward(self.dim_feedforward, dropout=dropout_p)
        self.layer_norm1 = LayerNorm(d_model)  # The normalization layer before the output of the PFFN layers
        self.layer_norm2 = LayerNorm(d_model)  # The normalization layer after the output of the PFFN layers
 
    def forward(self, x):
        # Shape: [batch_size, sequence_length, input_dim]
        batch_size = x.shape[0]
        length = x.shape[1]

        # Calculate the query and key vectors
        q = self.attention(x, x, x, mask=None)[0].reshape([batch_size, -1, self.heads, self.head_dim])  # Shape: [batch_size, sequence_length, heads*head_dim]
        k = self.attention(x, x, x, mask=None)[1].reshape([batch_size, -1, self.heads, self.head_dim])  # Shape: [batch_size, sequence_length, heads*head_dim]

        # Calculate the values for attention computation
        v = self.attention(x, x, x, mask=None)[2].reshape([batch_size, -1, self.heads, self.head_dim])  # Shape: [batch_size, sequence_length, heads*head_dim]

        # Calculate the query and key vectors
        q *= self.scale  # Scale the query
        k *= self.scale  # Scale the key

        # Calculate the output vectors from PFFN layers
        out = self.positionwise_feedforward(q @ k)
        out = self.layer_norm1(out)

        for i in range(self.num_layers):
            out = self.attention(out, out, out, mask=None)[0].reshape([batch_size, -1, self.heads, self.head_dim])  # Shape: [batch_size, sequence_length, heads*head_dim]
            out *= self.scale  # Scale the output

        return self.layer_norm2(out)


# Initializing the model
m = Model(d_model=10, heads=4, dim_feedforward=500)

