
class MultiheadAttention(torch.nn.Module):
    def __init__(self,
                 input_dim: int = 3,
                 num_heads: int = 8,
                 output_dim: int = 16,
                 dropout_p: float = 0.5):
        super().__init__()
 
        self.query_layer = torch.nn.Linear(input_dim, input_dim)
        self.key_layer = torch.nn.Linear(input_dim, input_dim)
        self.value_layer = torch.nn.Linear(input_dim, input_dim)

        self.attention_head = torch.nn.ModuleList([
            torch.nn.Linear(input_dim, output_dim) for _ in range(num_heads)])
 
        self.dropout = torch.nn.Dropout2d(p=dropout_p)
        self.out_layer = torch.nn.Linear(output_dim * num_heads, input_dim)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):

        # Query
        query = self.query_layer(query)  # shape=[N, d_q, H, W]
        assert query.shape[-1] == len(self.attention_head), \
            'Invalid length of the output dimension'
 
        # Key
        key = self.key_layer(key)  # shape=[N, d_k, H, W]
        assert key.shape[-1] == len(self.attention_head), \
            'Invalid length of the output dimension'

        # Value
        value = self.value_layer(value)  # shape=[N, d_v, H, W]
        assert value.shape[-1] == len(self.attention_head), \
            'Invalid length of the output dimension'
 
        # Attention
        for i in range(len(self.attention_head)):
            qk = query[:, :, i:i + 1, :] @ self.attention_head[i].T

            attn = torch.nn.functional.softmax(qk / math.sqrt(input_dim), dim=-2) #shape=[N, H, W]
            
            output = self.dropout(attn @ value[:, :, i:i + 1, :]) # shape=[N, H, W]
            output = output.flatten(-2).transpose(-1, -2)  # [N, d_k, N, d_v], permute the second dim to be last

            value[:, :, i:i + 1, :] = output
        output = self.out_layer(value)  # shape=[N, H, W, d_v]

        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = MultiheadAttention()
 
    def forward(self, x1, x2):
 
        # Query and key
        query  = x1
        key     = x2
 
        # Attention
        output = self.attention_layer(query, key, value)

        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
x2 = torch.randn(3, 8, 64, 64)
