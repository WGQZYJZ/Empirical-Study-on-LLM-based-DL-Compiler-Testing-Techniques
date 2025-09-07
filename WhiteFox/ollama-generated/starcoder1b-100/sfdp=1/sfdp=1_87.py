
class Model(torch.nn.Module):
    def __init__(self, hidden_size, num_attention_heads):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(hidden_size, hidden_size)
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.self_attention = SelfAttention(hidden_size, num_attention_heads, dropout=dropout_p)
        self.linear2 = torch.nn.Linear(num_attention_heads * hidden_size, 10)

    def forward(self, x1):
        qk = self.self_attention(query=x1, key=x1, value=x1)
        output = self.dropout(qk)
        output2 = self.linear(output) + 5
        return output2

# Initializing the model
m = Model(hidden_size, num_attention_heads)


