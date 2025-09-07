
class Model(torch.nn.Module):
    def __init__(self, query_key_size=64, num_attention_heads=12):
        super().__init__()
        self.query = torch.nn.Linear(query_key_size, query_key_size)
        self.keys = torch.nn.Linear(query_key_size, query_key_size)
        self.value = torch.nn.Linear(query_key_size, query_key_size)
        self.dropout = torch.nn.Dropout(p=0.5)
        self.attention = torch.nn.Linear(query_key_size * num_attention_heads, query_key_size)
 
    def forward(self, x):
        k = self.keys(x).view(-1, 32, 64, 8) # Shape [batch, head, length, dim]
        v = self.values(x).view(-1, 32, 64, 8) # Shape [batch, head, length, dim]
        qk = torch.matmul(self.query(x), k) # Shape [batch, length, query_key_size]
        scaled_qk = qk / math.sqrt(self._dim_per_head)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # Shape [batch, length, query_key_size]
        output = dropout_qk.matmul(v).transpose(-2, -1) # Shape [batch, head, length, dim]
        attention_output = torch.matmul(self.attention(x), output) # Shape [batch, length, query_key_size]
        scaled_attention_output = attention_output / math.sqrt(self._dim_per_head)
        output = torch.nn.functional.softmax(scaled_attention_output, dim=-1)
        dropout_output = torch.nn.functional.dropout(output, p=0.5) # Shape [batch, length, query_key_size]
        attention_output = torch.matmul(v, dropout_output).transpose(-2, -1) # Shape [batch, head, length, dim]
        return attention_output.view(-1, 64 * self._num_attention_heads, x.shape[2], x.shape[3])
 
    @property
    def _dim_per_head(self):
        return self._query_key_size // self._num_attention_heads
 
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 64 * m._num_attention_heads, 32, 64)
