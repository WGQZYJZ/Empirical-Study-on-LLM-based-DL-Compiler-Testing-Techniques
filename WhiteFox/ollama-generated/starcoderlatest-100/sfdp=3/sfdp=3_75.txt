
class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)

# Inputs to the model
query  = torch.randn(4, 8, 64, 64) # Query tensor of shape (batch_size x heads x seq_length x feature_dim). The values for a given head correspond to each other and should have the same length as the query sequence.
key    = torch.randn(4, 8, 64, 64) # Key tensor of shape (batch_size x heads x seq_length x feature_dim). The values for a given head correspond to each other and should have the same length as the key sequence.
value  = torch.randn(4, 8, 64, 64) # Value tensor of shape (batch_size x heads x seq_length x feature_dim). The values for a given head correspond to each other and should have the same length as the value sequence.
