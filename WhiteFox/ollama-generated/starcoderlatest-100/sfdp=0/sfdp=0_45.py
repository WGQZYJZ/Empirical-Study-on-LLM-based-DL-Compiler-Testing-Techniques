
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim, scale=None):
        super().__init__()
        self.dim = dim
        if not scale:
            self.scale = math.sqrt(dim)
        else:
            self.scale = scale

    def forward(self, q, k, v, batch_size, seq_length, heads):

        # The input shape is: [batch_size, seq_length, head_num * dim]
        # For attention weights of different shapes, use the following command in Pytorch 1.8 (only for Transformer models).
        # q = F.unfold(q, kernel_sizes=[2, 3], dilation=[1, 1])
        # k = F.unfold(k, kernel_sizes=[2, 3], dilation=[1, 1])

        query = self._split(q, batch_size)
        key = self._split(k, batch_size)
        value = self._split(v, batch_size)
        query = self._reshape(query)
        key = self._reshape(key)
        value = self._reshape(value)

        # Calculate the scaled dot-product attention between all pairs of queries and keys.
        # `matmul` is an operator for matrix multiplication that uses broadcasting when possible, but falls back to general (non-broadcasting) kernel on CPU and CUDA if needed.
        # https://pytorch.org/docs/stable/notes/numerical_accuracy.html#scaling-invariant-attention-softmax
        attention_scores = torch.matmul(query, key.transpose(-2, -1)) / self.scale

        # Calculate the softmax of all pairs of queries and keys for each example.
        # `softmax` is an operator that computes the softmax of a one-dimensional tensor or two-dimensional tensor with the given dimension along which it is applied.
        # `torch.exp()` performs elementwise exponentiation on the input Tensor. The output Tensor contains e^(x1) * ... * e^(xn) for each x1, ..., xn in input Tensor.
        # https://pytorch.org/docs/stable/_modules/torch/nn/functional.html#softmax
        attention_weights = torch.exp(attention_scores).softmax(dim=-1)

        # Calculate the weighted sum of all values across all heads for each example based on their attention weights and concat them into a single vector.
        output = attention_weights.matmul(value).transpose(-2, -1)
        return self._join(output, batch_size)

    def _split(self, t, batch_size):
        