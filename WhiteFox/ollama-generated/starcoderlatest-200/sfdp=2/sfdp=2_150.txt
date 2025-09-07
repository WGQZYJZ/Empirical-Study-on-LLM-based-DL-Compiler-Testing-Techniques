
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=self.config["attention_key"], 
            num_heads=self.config["num_attention_heads"])
    
    def forward(self, query, key, value):
        _, _output, attention = self.attn(query, key, value)
        scaled_output = _output / math.sqrt(attention.shape[-1]) 
        return scaled_output

# Initializing the model with required config
config = {
    "attention_key": 64, 
    "num_attention_heads": 8,
    "hidden_dim": 512}
m = Model(config)
# Inputs to the model
query = torch.randn(1, 3, 256, 256)
key = torch.randn(1, 3, 64, 64)
value = torch.randn(1, 3, 64, 64)
