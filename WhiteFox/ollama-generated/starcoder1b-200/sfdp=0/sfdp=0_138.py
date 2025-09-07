
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=-1):
        super().__init__()
        self.scale = dim ** -0.5

    def forward(self, qk, k, v):
        batch_size, length, _ = qk.shape

        # Transpose the attention tensors to be compatible with ScaledDotProductAttention's input requirements.
        qk = torch.transpose(qk, 1, self.scale)

        # Perform the forward pass of the Scaled Dot-Product Attention layer: `scaled_dot_product` and return `attention`.
        scaled_dot_product = torch.matmul(qk, k.transpose(-2, -1)) / self.scale

        attention = torch.softmax(scaled_dot_product, dim=self.scale)

        # Transpose the weights back to their original dimensions (batch, time, feature)
        output = torch.matmul(attention, v)
        return output


# Initializing the model
m = ScaledDotProductAttention()


