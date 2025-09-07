
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=8, intermediate_size=1024, hidden_size=768):
        super().__init__()

        self.num_attention_heads = num_attention_heads
        self.d_k = 64
        self.d_v = 1024
        self.dropout = torch.nn.Dropout(dropout_p)
        self.self_attn = MultiheadAttention(hidden_size=hidden_size, d_k=self.d_k, num_attention_heads=self.num_attention_heads)
        self.value = torch.nn.Linear(hidden_size, hidden_size, bias=True)
        self.key = torch.nn.Linear(hidden_size, hidden_size, bias=True)

    def forward(self, x):

        query = x.shape[-1]  # Number of features in the query tensor
        key = x.shape[-2]     # Number of features in the key tensor
        value = x.shape[-3]   # Number of features in the value tensor

        k = self.key(x).transpose(-2, -1)
        v = self.value(x).transpose(-2, -1)

        scores = self.self_attn((q=k, k=k, v=v))
        attention = F.softmax(scores, dim=-1)  # Softmax the results
        context = attention @ v  # Multiply the output of the softmax by the value.
        output = self.dropout(context)  # Apply dropout to the result

        return output


# Initializing the model
m = Model()
x = torch.randn(1, 3, 64, 64)
