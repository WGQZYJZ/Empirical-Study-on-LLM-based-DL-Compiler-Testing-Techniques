
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(768, 3 * 3 * 128, bias=False)

    def forward(self, x):
        # Shape of the output: B, T, C_model * K, H * W
        qk = self.qkv(x).chunk(3, dim=-1)
        attn_weight = torch.softmax(qk[0] + qk[2], dim=-1)  # Compute the dot product of the attention weights and the value

        value = torch.cat([
            attn_weight @ x[..., None],  # The first token is always self
            attn_weight @ x[:, :, None, :],
            attn_weight @ x[:, :, :, None]
        ], dim=-1)  # Concatenate the results of all three heads into a single value

        return value


# Initializing the model
m = Model()


