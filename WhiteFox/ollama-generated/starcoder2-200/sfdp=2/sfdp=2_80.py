
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_qk  = torch.nn.functional.normalize(query)@torch.nn.functional.normalize(key).transpose(-2, -1)
        # Compute the dot product of the normalized query and the normalized key 
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
 
        output  = dropout_qk@value
        return output


# Initializing the model
m  = Model()
 
# Inputs to the model
input_size  = (1024*8,) # Input size of the query is (1024, 8), 8 is the number of heads. And for the value and key both input sizes are equal to one. The size of these matrices are also equal to 64.
query  = torch.randn(input_size)
key   = torch.randn(*input_size)
value = torch.randn(*input_size)
 
__output__  = m(query, key, value)

