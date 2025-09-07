
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads=128):
        super().__init__()
        self.d_k = d_model // num_heads  # Key dimensionality in the attention mechanism
        self.d_v = d_model // num_heads  # Value dimensionality in the attention mechanism
        self.num_heads = num_heads
        assert d_k % num_heads == 0, "Invalid key dimensionality"

        self.wq = torch.nn.Linear(
            d_model, d_model, bias=False)  # Query part of the multi-head attention model (input: input tensor, output: query tensor)
        self.wk = torch.nn.Linear(
            d_model, d_k * num_heads, bias=False)  # Key part of the multi-head attention model (input: input tensor, output: key tensor)
        self.wv = torch.nn.Linear(
            d_model, d_v * num_heads, bias=False)  # Value part of the multi-head attention model (input: input tensor, output: value tensor)

    def forward(self, x):
        # Input: [batch size] [d_model]
        batch_size = x.shape[0]
        q = self.wq(x).view(batch_size, -1, self.num_heads, self.d_k)  # Compute the query tensor from the input tensor
        k = self.wk(x).view(batch_size, -1, self.num_heads, self.d_k)  # Compute the key tensor from the input tensor
        v = self.wv(x).view(batch_size, -1, self.num_heads, self.d_v)  # Compute the value tensor from the input tensor

        qk = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)
        softmax_qk = softmax(qk)
        dropout_qk = torch.nn.functional.dropout(
            softmax_qk, p=0.2)  # Apply dropout to the softmax output

        output = (
            torch.matmul(dropout_qk, v)
            .transpose(-2, -1)
            .contiguous()
            .view(batch_size, -1, self.d_model))  # Compute the attention result tensor
        return output


# Initializing the model
m = MultiHeadAttention(128)

# Inputs to the model
x1 = torch.randn(1, 128)
