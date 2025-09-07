
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, value)
        scaled_qk = qk[0] / (1.0 / 2 ** 0.5)
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3)
        output = self.attention(query, key, dropout_qk * value)[0]
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 64, 256) # query with shape (batch_size x sequence_length x input_feature_dim)
x2  = torch.randn(8,  32, 1024) # key with shape (num_heads x sequence_length x input_feature_dim)
x3  = torch.randn( 8,   64,  512) # value with shape (num_heads x sequence_length x output_feature_dim)
