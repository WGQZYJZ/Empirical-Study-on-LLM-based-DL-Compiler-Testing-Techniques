
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model: int, num_heads: int):
        super().__init__()

        self.num_heads = num_heads
        assert d_model % self.num_heads == 0 # must be divisible by the number of heads
        self.d_head = d_model // self.num_heads # dimension of a single head
 
        self.depthwise_conv = torch.nn.Conv2d(
            in_channels=3, 
            out_channels=self.num_heads, 
            kernel_size=1,
            stride=1,
            padding=0, 
        )

        self.linear = torch.nn.Linear(in_features=self.num_heads, out_features=d_model)
        self.dropout = torch.nn.Dropout(p=0.2)

    def forward(self, x: Tensor):
        # The tensor is now of shape (batch_size, num_heads, depthwise_conv, height, width), where the batch_size and channel dimension has been squeezed out. 
        x = self._depthwise_conv(x)

        # Shape of tensor in which attention weights are computed from scaled dot product of query and key tensors
        _attention_weights = torch.matmul(self._linear(x).permute(0, 2, 1), self._linear(key).transpose(-2, -1)) / (1e-5 + torch.norm(self._linear(key), dim=-1) ** 2)
        attention_weights = torch.nn.functional.softmax(_attention_weights, dim=-1)

        # Shape of tensor used to compute the weighted sum of the value tensors
        _value = self._linear(x).permute(0, 2, 1)
        value = torch.matmul(attention_weights, _value)
 
        return (self._dropout(value), attention_weights)
 
    def _depthwise_conv(self, x: Tensor):
        