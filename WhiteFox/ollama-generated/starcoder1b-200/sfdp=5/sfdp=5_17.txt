
class Model(torch.nn.Module):
    def __init__(self, num_heads):
        super().__init__()
        self.layer = nn.TransformerEncoderLayer(num_heads=num_heads)
 
    def forward(self, x1):
        attn  = torch.zeros((batch_size, seq_length, seq_length))
        for i in range(batch_size):
            for j in range(seq_length):
                attention  = self.layer.get_attn_weights(x1[i][j], x1[i][:].unsqueeze(-1).expand(-1, seq_length, seq_length))
                attn[i][j] = attention
        output = attn  @ value  # Compute the dot product of the dropout output and the value

# Initializing the model
m = Model(num_heads=4)


