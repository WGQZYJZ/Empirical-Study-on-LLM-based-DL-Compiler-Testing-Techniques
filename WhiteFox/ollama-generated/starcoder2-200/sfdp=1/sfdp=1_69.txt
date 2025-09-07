
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
 
        # Compute dot product between `query` and `key`, scale the result by an inverse scale factor and apply softmax 
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1)
 
        # Apply dropout to the result of softmax computation
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        # Compute dot product between `value` and `dropout_qk`
        output  = dropout_qk.matmul(value)
        return output

# Initializing the model
m  = Model()
 
# Inputs to the model
query1  = torch.randn(32, 64, 8, 8)
key1  = torch.randn(32, 64, 8, 8)
value1  = torch.randn(32, 512, 8, 8)
 
query2  = torch.randn(32, 64, 80, 80)
key2  = torch.randn(32, 64, 80, 80)
value2  = torch.randn(32, 512, 80, 80)
 
# Output for model with input query of shape (batch_size x embedding_dim x query_sequence_length x key/value sequence length). Shape could be: (32, 64, 8, 8), or (32, 512, 80, 80)
__output_1__  = m(query1, key1, value1)
 
# Output for model with input query of shape (batch_size x embedding_dim x query_sequence_length x key/value sequence length). Shape could be: (32, 64, 80, 80), or (32, 512, 80, 80)
__output_2__  = m(query2, key2, value2)

