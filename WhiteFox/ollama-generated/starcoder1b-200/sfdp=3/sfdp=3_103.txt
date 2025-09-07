
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, dim_k=256):
        super().__init__()
        self.scale_factor = torch.sqrt(dim_k / num_heads)
        self.num_heads = num_heads
        self.attn = Attention(dim_q=dim_k // 2, dim_v=dim_k // 2)

    def forward(self, x1):
        # ...
        output = x1 * self.scale_factor  # Apply a pointwise convolution with a scale factor to the input tensor
        output = self.attn.attention(query=output, key=output)  # Compute the attention weighted sum
        output = torch.nn.functional.dropout(output, p=dropout_p)  # Apply dropout to the weighted output
        return output


# Initializing the model
m = Model()


