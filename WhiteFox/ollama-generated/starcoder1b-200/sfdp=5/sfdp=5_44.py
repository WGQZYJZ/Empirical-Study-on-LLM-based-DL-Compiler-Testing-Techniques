
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead, num_encoder_layers=6, num_decoder_layers=6):
        super().__init__()
        self.attn = torch.nn.MultiHeadAttention(d_model, nhead)  # Multi-Head Attention Model

        self.position_encoding = torch.nn.Embedding(max_len, d_model)

    def forward(self, x1):
        qk = self.pos_encoding @ x1
        k = x1.view(-1, x1.size(1))  # Convert to (batch * seq_length, input_dim)

        v = self.attn(q=qk, k=k, v=k)  # Compute the dot product of the query and key
        v = torch.dropout(v, dropout_p, True)
        output = self.value @ v  # Apply the dot product to the attention weights
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 64, 64)
