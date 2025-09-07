
class Attention(torch.nn.Module):
    def __init__(self, input_size, num_heads, hidden_dim):
        super().__init__()
        self.num_attention_heads = num_heads
        self.attention_head_size = int(input_size / num_heads)
        self.all_linear = torch.nn.Linear(hidden_dim, 3 * hidden_dim)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # compute the dot product of the query and the key
        scaled_qk = qk / np.sqrt(float(self.attention_head_size)) # scale the dot product by the inverse scale factor
        softmax_qk = F.softmax(scaled_qk, dim=-1)  # apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # apply dropout to the softmax output
        output = torch.matmul(dropout_qk, value)  # compute the dot product of the dropout output and the value
        return self.all_linear(output).view(-1, 3 * self.attention_head_size)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = Attention(8, 4, 512)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        attention_output = self.attention(v6, v6, v6)
        return attention_output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
