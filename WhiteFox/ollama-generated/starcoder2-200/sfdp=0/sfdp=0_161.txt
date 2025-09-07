
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config: Config, dropout=None):
        super().__init__()
        self._query = torch.nn.Linear(config['d_k'], config['d_k'])
        self._key = torch.nn.Linear(config['d_k'], config['d_k'])
        self._value = torch.nn.Linear(config['d_model'], config['d_model'])
 
        self._softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key):
        scaled_dot_product  = self._query(query).matmul(self._key(key).transpose(-2,-1)) / math.sqrt(query.shape[-1]) 
        attention_weights = self._softmax(scaled_dot_product)
        return attention_weights.matmul(value)


# Initializing the model
sdp_attn  = ScaledDotProductAttention({
    'd_model':64, 
    'd_k':32,  
    'd_v':16})


# Inputs to the model (query and key tensors)
input_query  = torch.randn(50, 8, 32)
input_key  = torch.randn(50, 8, 32)
 
