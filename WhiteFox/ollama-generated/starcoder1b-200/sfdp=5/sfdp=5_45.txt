
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(4096, 50)
 
    def forward(self, x1):
        query = m.conv(x1).view(-1, self.num_attention_heads,
                                 (query.size(-2) / self.num_attention_heads),
                                 (query.size(-1) / self.num_attention_heads), 8)
        key   = m.conv(self.key).view(-1, self.num_attention_heads,
                                 (key.size(-2) / self.num_attention_heads),
                                 (key.size(-1) / self.num_attention_heads), 8)
        query = torch.tanh(query)
        key   = torch.tanh(key)
        attn = torch.bmm(query, key).view(
            -1, self.num_attention_heads, (query.size(-2) / self.num_attention_heads), (query.size(-1) / self.num_attention_heads))
        attn = torch.softmax(attn, dim=-1)
        value = m.conv(self.value).view(-1, self.num_attention_heads,
                                    (value.size(-2) / self.num_attention_heads),
                                    (value.size(-1) / self.num_attention_heads), 8)
        output = torch.bmm(attn, value).view(
            -1, self.hidden_size) + self.fc(output)
        return output


# Initializing the model
m = Model()


