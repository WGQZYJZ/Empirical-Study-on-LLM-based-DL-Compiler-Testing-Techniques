
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, k1, v0):
        # Get the scale factor from `v0` by computing the square root of the maximum element in `v0`.
        inv_scale = torch.max(v0).sqrt()

        key  = k1 * inv_scale
        value = v0

        # Compute Scaled Dot-Product Attention.
        scaled_dot_product = torch.matmul(query, key) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)

        # Multiply the weighted sum of `v0` and compute output.
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m  = Model()

