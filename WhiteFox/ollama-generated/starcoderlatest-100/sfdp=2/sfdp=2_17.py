
class MultiheadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads=8, dropout_p=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads  # output dimensions of query and key
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / math.sqrt(self.d_model) # Scale the dot product by sqrt(output dimension)
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk @ value
        return output


# Initializing the model
attention = MultiheadAttention(d_model=512, num_heads=8, dropout_p=0.3)

# Inputs to the model
q = torch.randn(1, 4096, 768) # shape of query [batch size, input sequence length, query dimension]
k = torch.randn(1, 256, 768) # shape of key [batch size, number of keys per head, key dimension]
v = torch.randn(1, 256, 768) # shape of value [batch size, number of values per head, value dimension]


# Performing the forward pass of MultiheadAttention
