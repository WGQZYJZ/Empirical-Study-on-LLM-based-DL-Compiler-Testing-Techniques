
class Model(torch.nn.Module):
    def __init__(self, scale_factor=1, num_attention_heads=8, key_dim=32):
        super().__init__()
 
        self.scale_factor = scale_factor
        self.num_attention_heads = num_attention_heads
        self.key_dim = key_dim

        # We create a linear layer with self.key_dim input features to self.num_attention_heads attention heads with 
        # 16 as the number of output features per head and apply a softmax function to normalize the weights in 
        # each head. For this example, we can assume that our key tensor has shape (batch size, max sequence length, 
        # query dimension) and query tensor has shape (batch size, max sequence length, value dimension).
        self.key_layer = torch.nn.Linear(self.key_dim, num_attention_heads * 16, bias=False)
        self.query_layer = torch.nn.Linear(key_dim, num_attention_heads * 16, bias=False)
        self.softmax_layer = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key):
        # The keys tensor has shape (batch size, max sequence length, query dimension) and the values tensor 
        # has shape (batch size, max sequence length, value dimension). So we need to transpose the input tensor 
        # if the dimensions of them are not in proper order. Here, all three tensors have a single first dimension, so 
        # we can simply transpose it.
        key = self.key_layer(query.transpose(-2, -1))
 
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(self.scale_factor)  # Scale the dot product by a factor
        softmax_qk = self.softmax_layer(scaled_qk)  # Apply softmax to the scaled dot product
 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.125)  # Apply dropout to the softmax output
 
        output = dropout_qk.matmul(key)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4, 20, 8)
x2 = torch.randn(4, 32, 256)
