
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.query = torch.nn.Linear(config.vocab_size, config.hidden_size)
        self.key = torch.nn.Linear(config.vocab_size, config.hidden_size)
        self.value = torch.nn.Linear(config.hidden_size, config.vocab_size)
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, input_tensor):
        # Query layer
        query  = self.query(input_tensor)
        # Key and Value layers
        key    = self.key(input_tensor)
        value  = self.value(input_tensor)
        # Scale dot product (query @ key / sqrt(query.size(-1)))
        query_dot_key = torch.matmul(query, key) / math.sqrt(input_tensor.size(-1))
        attn_mask  = torch.triu(torch.ones((self.config.hidden_size, self.config.hidden_size), dtype=torch.float32)).type_as(query_dot_key)

        # Apply dropout to attention weights and value (scaled dot product + dropout)
        attn_weights  = self.softmax(query_dot_key)
        output        = attn_weights @ value
        return output


# Initializing the model
m = Model(config)
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
