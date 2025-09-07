
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, query, key, value):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / (math.sqrt(self.attention.embed_dim) * math.sqrt(256))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = self.attention(dropout_qk, value)[0]  # This returns (output, attention_weights). Only the first element is used for inference
        return output


# Initializing the model
m = Model()
query = torch.randn(1, 16, 32, 32)
key   = torch.randn(1, 16, 32, 32)
value = torch.randn(1, 16, 80, 80)
# Applying the model to the model
