
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale):
        super().__init__()
        self.softmax = torch.nn.Softmax(-1)
        self.inv_scale  = inv_scale
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights  = self.softmax(scaled_dot_product)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
model  = ScaledDotProductAttention()

# Inputs to the model
query1  = torch.randn(4,32,600,600) # Shape (4, batchsize, query_length, query_depth)
key1  = torch.randn(4,32,600,600)# Shape (4, batchsize, key_length, key_depth)
value1  = torch.randn(4,32,768) # Shape (batchsize, value_length, value_depth)


