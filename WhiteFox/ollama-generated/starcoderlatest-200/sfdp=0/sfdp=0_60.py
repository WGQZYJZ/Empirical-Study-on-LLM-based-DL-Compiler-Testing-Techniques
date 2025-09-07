
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, n_channels=256):
        super().__init__()
        self.n_channels = n_channels

    def forward(self, query, key):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / (math.sqrt(self.n_channels))
        attention_weights   = ScaledDotProductAttention.apply(query, key, self.n_channels)
        output              = attention_weights.matmul(value)
        return output

    @staticmethod
    def apply(query, key, n_channels):
        # Input dimensions: (batch_size, query_height, query_width, channels), 
        # (batch_size, key_height, key_width, channels), and (batch_size, num_key_blocks * num_value_blocks, key_height, key_width, value_channels)
        query = torch.unsqueeze(query, dim=1).transpose(-2,-3)

        # Output dimensions: (batch_size, query_height, query_width, channels), 
        # (batch_size, key_height, key_width, channels), and (batch_size, num_key_blocks * num_value_blocks, key_height, key_width, value_channels)
        key = torch.unsqueeze(key, dim=1).transpose(-2,-3)

        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / (math.sqrt(n_channels))

        # Output dimensions: (batch_size, num_key_blocks * num_value_blocks, query_height, query_width), 
        # and (batch_size, num_key_blocks * num_value_blocks)
        scaled_dot_product = scaled_dot_product.permute(0, 2, 3, 1)

        # Output dimensions: (batch_size, num_key_blocks * num_value_blocks, query_height, query_width), 
        # and (batch_size, num_key_blocks * num_value_blocks)
        scaled_dot_product = scaled_dot_product.reshape(scaled_dot_product.shape[0], 
                                                            scaled_dot_product.shape[1], 
                                                            -1).permute(0,2,3,1)

        # Output dimensions: (batch_size * num_key_blocks * num_value_blocks), and (batch_size * num_key_blocks * num_value_blocks)
        scaled_dot_product = scaled_dot_product.flatten(start_dim=0).permute(1, 0)

        # Output dimensions: (batch_size * num_key_blocks * num_value_blocks), and (batch_size * num_key_blocks * num_value_blocks)
        attention_weights   = scaled_dot_product.softmax(dim=None)

        return attention_weights


class Model(torch.nn.Module):
    def __init__(self, n_channels=256):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scdpa = ScaledDotProductAttention(n_channels)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        output_1 = self.scdpa(query=v6, key=x1)
        return output_1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
m = Model()
