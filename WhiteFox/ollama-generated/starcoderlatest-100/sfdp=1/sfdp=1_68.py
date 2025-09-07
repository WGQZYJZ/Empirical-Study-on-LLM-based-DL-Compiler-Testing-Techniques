
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(128, 64)

    def forward(self, x_query, x_key, x_value):
        qk = torch.matmul(x_query, x_key.transpose(-2, -1)) # Compute the dot product of query and key tensors
        scaled_qk = qk / math.sqrt(self.attn.in_features) # Scale the dot product by sqrt(number of input features in the attention layer). In general, scaling is performed with `sqrt()` so that the values do not grow too large, which may hurt model performance.
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        output = torch.matmul(softmax_qk, x_value) # Compute the dot product of softmax output and value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x_query = torch.randn(2, 128, 64, 64) # This is an input query of shape (batch size, number of attention heads for query tensor, query length/width, query length/width). In general, if there are `n` attention heads, the shape should be `(batch_size, n, query length / head dimension, query length / head dimension)`.
x_key = torch.randn(2, 128, 64, 64) # This is an input key of shape (batch size, number of attention heads for key tensor, query length/width, query length/width). In general, if there are `n` attention heads, the shape should be `(batch_size, n, key length / head dimension, key length / head dimension)`.
x_value = torch.randn(2, 128, 64, 64) # This is an input value of shape (batch size, number of attention heads for query tensor, query length/width, query length/width). In general, if there are `n` attention heads, the shape should be `(batch_size, n, key length / head dimension, key length / head dimension)`.
