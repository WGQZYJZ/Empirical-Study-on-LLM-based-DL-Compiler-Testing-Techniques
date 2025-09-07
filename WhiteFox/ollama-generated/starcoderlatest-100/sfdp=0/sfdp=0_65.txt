
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=128, num_heads=3, n_head_attention=16):
        super().__init__()
        self.num_layers = 4
        self.embed_dim = 512

        # Multi-head self attention layers
        for i in range(0, self.num_layers - 1):
            setattr(self, f'att_{i}', torch.nn.MultiheadAttention(self.embed_dim, num_heads))
            setattr(self, f'norm_{i}', nn.LayerNorm(512))

    def forward(self, query, key, value):
        x = self._pre_process([query, key])
        for i in range(0, self.num_layers - 1):
            x[f'att_{i}'].forward_qkv(x[f'norm_{i}'], x[f'{i}_attn'])
        
        # Compute attention weights
        query = x[f'att_{self.num_layers - 1}'].attention_output

        # Multiply the output of self-attention by the value tensor to get new context vector
        attention_weights = torch.softmax(query, dim=-1)
        output = attention_weights.matmul(value)
        
        return output

    def _pre_process(self, input_tensor):
        norms = nn.LayerNorm(input_tensor[0].size())
        return [
            {'norm': norms},
            *[{
                'attn': getattr(getattr(nn, name), attr).forward(x1=getattr(input_tensor, k)[f'norm'], x2=getattr(input_tensor, l)[f'norm'])
            } for k, v in self.__dict__.items() if f'{k}_attn' in v]
        ]


# Initializing the model
m = Model(hidden_dim=16)

# Inputs to the model
query  = torch.randn(8, 32, 512)
key    = torch.randn(8, 32, 512)
value  = torch.randn(8, 32, 512)
