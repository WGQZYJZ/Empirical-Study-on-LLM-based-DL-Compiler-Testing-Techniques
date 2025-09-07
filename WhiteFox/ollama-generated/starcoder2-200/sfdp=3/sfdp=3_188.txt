
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v4  = torch.matmul(query1, key2.transpose(-2, -1))
        v5  = v4 * scale_factor
        v6  = v5.softmax(dim=-1)
        v7  = dropout_qk = torch.nn.functional.dropout(v6, p=dropout_p) 
        return v7

# Initializing the model
m  = Model()
 
# Inputs to the model
query1  = torch.randn(32, 8, 64, 64) # Shape (batch_size x head_num x sequence_length x hidden_size / head_dim)
key2   = torch.randn(32, 8, 64, 64) # Shape (batch_size x head_num x sequence_length x hidden_size / head_dim)
value3 = torch.randn(32, 8, 10, 5)  # Shape (batch_size x head_num x sequence_length x output_size / head_dim)
 
__output__  = m(query1, key2, value3)
