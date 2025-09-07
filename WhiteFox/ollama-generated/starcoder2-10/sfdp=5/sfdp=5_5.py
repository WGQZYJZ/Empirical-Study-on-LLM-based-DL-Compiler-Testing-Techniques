
class Model(torch.nn.Module):
    def __init__(self, num_layers=12, d_model=512, heads=8, dropout=0.1, dim_feedforward=2048, max_sequence_length=100):
        super().__init__()
 
        self.encoder = torch.nn.TransformerEncoderLayer(d_model=d_model, nhead=heads)
 
    def forward(self, query, key, value):
        v1  = self.encoder(query)
        v2  = torch.matmul(v1, torch.transpose(key, -1, -2)) / math.sqrt(d_model) 
        v3  = (v2 + key).transpose(-1, -2)
        v4  = torch.softmax(v3 * 0.5 ** 1e-6, dim=-1)
        v5  = torch.dropout(v4, dropout, True)
        v6  = torch.matmul(value, v5)
        return v6

# Initializing the model
m  = Model()
 
# Inputs to the model (for query and key)
query_input  = torch.randn(1024, max_sequence_length)   # batch size x max length of sequence
key_input    = torch.randn(3072, max_sequence_length)   # batch size x max length of sequence

# Inputs to the model (for value)
value_input  = torch.randn(1536, max_sequence_length)
 
__output__  = m(query_input, key_input, value_input)

