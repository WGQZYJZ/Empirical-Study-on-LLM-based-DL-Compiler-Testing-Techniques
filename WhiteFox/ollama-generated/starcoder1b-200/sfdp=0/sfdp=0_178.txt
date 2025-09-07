
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1).contiguous().view(-1, 8 * 3 * 64 * 64)  # (batch, time_steps, number_of_attention_heads, number_of_pixels)
        w1 = torch.cat((x1, x1), dim=2)
        w1 = self._layernorm(w1).contiguous().view(-1, 8 * 3 * 64 * 64)

        scaled_dot_product = torch.matmul(w1, w1.transpose(-2, -1)) / math.sqrt(
            float(self.num_attention_heads))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1).contiguous()

        return output


# Initializing the model
m  = Model()
