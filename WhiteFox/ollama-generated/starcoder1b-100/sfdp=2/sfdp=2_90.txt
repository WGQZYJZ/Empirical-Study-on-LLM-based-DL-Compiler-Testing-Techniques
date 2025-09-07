
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query = x2
        key = x1  # Note that here we use `x1` as the "key" and `x2` as the "query" tensor for simplicity.
        v = self.conv(query).unsqueeze(-2)  # (batch_size, num_heads, channels, height, width)
        k = torch.matmul(v, key.transpose(-2, -1))  # (batch_size, num_heads, query_length, key_length)
        s = torch.nn.functional.softmax(k.div(self.attention_dropout), dim=-1)
        v = dropout_attention(s, p=self.attention_dropout)  # (batch_size, num_heads, query_length, key_length) * (batch_size, num_heads, query_length, key_length) -> (batch_size, num_heads, query_length, key_length)
        return self.conv(v)  # (batch_size, channels, height, width)


# Initializing the model
m = Model()
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
