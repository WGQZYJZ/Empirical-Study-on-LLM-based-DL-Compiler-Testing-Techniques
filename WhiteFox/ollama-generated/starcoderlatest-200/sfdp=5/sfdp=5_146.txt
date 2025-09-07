
class Model(torch.nn.Module):
    def __init__(self, dim_q: int, dim_k: int, dim_v: int, dim_attn_proj: int, num_heads: int):
        super().__init__()

        self.dim_q = dim_q
        self.dim_k = dim_k
        self.dim_v = dim_v
        self.dim_attn_proj = dim_attn_proj
        self.num_heads = num_heads

        # Embedding layer for the query, key, and value
        embedding_layer = torch.nn.Linear(in_features=self.dim_q + self.dim_k + 2 * self.dim_attn_proj, out_features=4 * dim_v)
        self._embedding_layer = nn.Sequential(
            # Flatten the input
            nn.Flatten(),

            # Linear layer
            embedding_layer,
            nn.GELU()
        )

        # Transformer encoder blocks
        for _ in range(self.num_heads):
            # Embedding for the output of each block
            self.add_module("transformer_block_%d" % (1 + len(_)), EncoderBlock(dim_q=self.dim_v, dim_k=self.dim_v, dim_attn_proj=dim_attn_proj))

    def forward(self, x):
        # Split the input tensor into query and key
        q = torch.cat((x[:, :, :self.dim_q], x[:, :, self.dim_q: 2 * self.dim_q]), dim=-1)
        k = torch.cat((x[:, :, -self.dim_k:], x[:, :, :-self.dim_k]), dim=-1)

        # Apply the embedding layer
        x_embed = self._embedding_layer(x=x, q=q, k=k)
        
        # Transform the input tensor into attention weights (which is a matrix) and values (also called output) for all heads in the transformer encoder
        outputs = []
        for _ in range(self.num_heads):
            output = self._transformer_block_n(x=x_embed, head=_).transpose(1, 2)

            # Add the output to the list of outputs (this will be used later in the multi-head attention block)
            outputs += [output]
        
        # Concatenate and transpose each head's output into a single tensor
        attn = torch.cat(outputs, dim=0).transpose(0, 1)

        return attn


# Initializing the model
m = Model(dim_q=512, dim_k=64, dim_v=16, dim_attn_proj=32, num_heads=2)

# Inputs to the model
x1 = torch.randn(1, 8, 1024, 256)
