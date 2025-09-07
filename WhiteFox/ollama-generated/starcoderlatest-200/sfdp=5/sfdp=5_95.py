This pattern characterizes the transformer models as described in [Attention is all you need](https://arxiv.org/abs/1706.03762).


# Model
class AttentionLayer(torch.nn.Module):
    def __init__(self, num_attn_heads: int = 8, dropout_p: float = 0.1):
        super().__init__()

        self.layer_norm_q = torch.nn.LayerNorm(normalized_shape=[576])
        self.conv_qkv_q = torch.nn.Conv2d(in_channels=384, out_channels=576, kernel_size=(1, 1), stride=1, padding=(0, 0))

        # Attention Heads
        self.attn_layer_norm_1 = torch.nn.LayerNorm(normalized_shape=[288])
        self.attn_conv_qkv_1 = torch.nn.Conv2d(self._)
