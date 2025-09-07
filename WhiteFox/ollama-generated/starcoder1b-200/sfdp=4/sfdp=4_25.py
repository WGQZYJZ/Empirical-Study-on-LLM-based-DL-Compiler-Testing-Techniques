
class Model(torch.nn.Module):
    def __init__(self, qkv_dims):
        super().__init__()
        self.qkv_dims = qkv_dims  # Query/key/value dimensions
        assert self.qkv_dims % 3 == 0
        assert self.qkv_dims >= 6, "Query/key/value dims {} is not supported.".format(self.qkv_dims)
        self.qkv = torch.nn.Linear(qkv_dims, qkv_dims // 3)  # Query, key and value tensors are concatenated
        self.attn_mask = torch.nn.Parameter(torch.ones(1, 64, 64), requires_grad=True)  # Initialize the attention mask for the position
        self.proj = torch.nn.Linear(qkv_dims // 3, qkv_dims)  # Output tensors are concatenated
        self.ln_norm = torch.nn.LayerNorm(qkv_dims)  # The layer normalizer

    def forward(self, x):
        # First concat the query and key to make a tensor with shape (batch size, depth * 3, num features of all inputs)
        qk = self.qkv(x).chunk(3, dim=-1)  # Split them into query, key and value tensors
        k, v, w = torch.split(qk[0], [self.qkv_dims // 3, self.qkv_dims // 3], dim=1)  # Get the last two tensors from qk

        # Then concatenate to make a tensor with shape (batch size, depth * 64, 3)
        attn = torch.cat((k, v), dim=-2)  # Concatenate along dimension -1
        # Normalize by sqrt(depth * width * height). Use the mean instead of std here because the attention weights are normalized.
        attn_weight = torch.softmax(attn / math.sqrt(self.qkv_dims // 3))
        # Multiply each element in the output by its corresponding attention weight, and normalize it along dimension -2 to make a tensor with shape (batch size, depth * 64)
        weighted_sum = self.proj(attn_weight @ v)  # Calculate the weighted sum of the value tensors

        # Then apply layer normalizer on the resultant tensor so that it follows the same normal distribution as the input data
        ln_norm_output = self.ln_norm(weighted_sum)

        return ln_norm_output


# Initializing the model
m  = Model()

