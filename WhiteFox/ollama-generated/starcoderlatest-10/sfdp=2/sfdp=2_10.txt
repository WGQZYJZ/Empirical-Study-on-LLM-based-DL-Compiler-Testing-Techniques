
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, head_num=8, num_attention_heads=16):
        super().__init__()
        self.head_num = head_num # number of heads in the multi-head attention mechanism.
        self.key_layer = torch.nn.Linear(3, head_num * 2 * num_attention_heads)
        self.value_layer = torch.nn.Linear(3, head_num * 2 * num_attention_heads)

    def forward(self, query, key, value):
        # 1. Compute the query and key for each heads in parallel by splitting input tensor into multi-head attention layers
        k0 = self.key_layer(query).reshape(query.shape[0], -1, self.head_num,
                                          2 * self.num_attention_heads)
        v0 = self.value_layer(key).reshape(key.shape[0], -1, self.head_num,
                                          2 * self.num_attention_heads)
        # 2. Compute the attention and concatenate multi-head attention layers to form output tensor
        # ...
        return output


# Initializing the model
m = MultiHeadSelfAttention()

