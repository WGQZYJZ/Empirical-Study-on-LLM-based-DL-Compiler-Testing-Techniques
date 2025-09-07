
class DotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):

        # Scaled Dot Product Attention: compute attention weights as the scaled dot product of the query and key vectors divided by a scaling factor.
        inv_scale = torch.rsqrt(torch.tensor([key.shape[-1]]))  # Scale the keys to be of unit length. (The reason we scale is because in the original implementation, 64-dimensional queries and keys are scaled to length sqrt(2)/2 to avoid large gradients during backpropagation.)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale

        # Scale the dot product attention weights by softmax
        attention_weights = scaled_dot_product.softmax(dim=-1)  # Compute the attention weights as a probability distribution over the columns of the value tensor. This is done using the softmax function on the dot-product result. We then normalize this vector to compute the probabilities that each row/column pair contributes to the output.

        # Add Attention Weights to Value Tensor
        output = attention_weights.matmul(value)  # The final output is computed by multiplying the weighted sum of all the columns in the value tensor with their corresponding attention weights as an elementwise product.

        return output

# Initializing the model
dot = DotProductAttention()


# Inputs to the model: 3 input tensors for query, key and values respectively. Shape is (batch_size, dim1, dim2), where batch size, dim1 and dim2 can be any positive integer that satisfies the requirements listed above.

query = torch.randn(20, 48)
key = torch.randn(576, 392)
value = torch.randn(728, 235)
