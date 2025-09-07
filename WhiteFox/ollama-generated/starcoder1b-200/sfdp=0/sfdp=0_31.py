
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # query, key and value are all tensors of shape (batch_size, seq_length, input_dim), which are the output tensor for the Transformer's multi-head attention. 
        # The key and value are the same shapes as the input to compute the attention weights, while the query is also a flattened batch_size * sequence_length vector,
        # which is computed by the following formulas:
        # query = x1.contiguous().view(-1, 3, 64, 64)  # Reshape the tensor of shape (batch_size * seq_length, input_dim) into a batch_size * seq_length vector of dimensionality (num_heads * input_dim).
        query = x1.contiguous().view(-1, 3, 64, 64).permute(2, 0, 1)  # Reshape the tensor of shape (batch_size * seq_length, input_dim) into a batch_size * seq_length vector of dimensionality (input_dim).
        key = x1.contiguous().view(-1, 8, 3, 3)  # Reshape the tensor of shape (batch_size * seq_length, output_dim) into a batch_size * seq_length vector of dimensionality (num_heads * output_dim).
        value = torch.randn(1, 8, 64, 64)  # Generate a random random-initialized tensor of shape (batch_size * seq_length, output_dim).
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self._num_attention_heads * x1.size(-1))  # Compute the scaled dot product between each pair of vectors in the query and key tensors, and then compute the softmax weights on the result.
        attention_weights = scaled_dot_product.softmax(dim=-1)  # Weights are computed as the softmax of the scaled dot product of the query and key tensors.
        output = attention_weights.matmul(value)  # The weighted sum of the value tensor is the output tensor for the Transformer's multi-head attention.
        return output


# Initializing the model
m = Model()


