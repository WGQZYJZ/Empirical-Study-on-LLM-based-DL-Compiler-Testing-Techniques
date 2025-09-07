
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.attention_module = torch.nn.MultiheadAttention(config["input_dim"], config["num_heads"])
 
    def forward(self, query, key, value):
        qk = self.attention_module(query, key=key)
        softmax_qk = qk / math.sqrt(config["input_dim"])
        return softmax_qk


# Configuration of the model 
config = {
    "num_heads": 16,
    "input_dim": 1024,
}

# Inputs to the model
query = torch.randn(32, config["num_heads"], 8, 1024)
key = torch.randn(32, config["num_heads"], 64, 1024)
value = torch.randn(32, config["num_heads"], 64, 1024)
