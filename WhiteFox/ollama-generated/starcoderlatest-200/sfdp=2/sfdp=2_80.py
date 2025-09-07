
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=16, attention_head_size=32, intermediate_size=1024):
        super().__init__()

        self.query = torch.nn.Linear(dim, dim)
        self.key   = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)

    def forward(self, x):
        q = self.query(x).view(-1, num_attention_heads, dim // num_attention_heads)
        k = self.key(x).view(-1, num_attention_heads, dim // num_attention_heads)
        v = self.value(x).view(-1, num_attention_heads, dim // num_attention_heads)

        # Apply attention on query and key, apply dropout in between
        qk = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(dim)
        attention_probs = F.softmax(qk, dim=-1)
        attention_probs = F.dropout(attention_probs, p=dropout_p)

        # Apply softmax in between to normalize the attention scores to weights
        out = (
            attention_probs.matmul(v).view(-1, num_attention_heads * dim)
                .transpose(0, 1)
                .contiguous()
        )

        out = self.fc(out)

        return out

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(8, 16, 512, 7)
