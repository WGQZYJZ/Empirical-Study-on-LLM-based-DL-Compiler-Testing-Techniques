
class SelfAttention(torch.nn.Module):
    def __init__(self, config: dict):
        super().__init__()
        self.linear = torch.nn.Linear(config["dmodel"], 3 * config["dmodel"])
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (3 ** 0.5)
        attention_weights = self.softmax(scaled_dot_product)
        output = torch.matmul(attention_weights, value)
        return output


# Initializing the model
m  = SelfAttention({
  "dmodel": 768, 
  "dkey":  128, 
  "dvocab":   4096
})
 
 # Inputs to the model
query = torch.randn(32, 64, 768)
key = torch.randn(32, 10, 768)
value = torch.randn(32, 5000, 768)

 # Initializing the model
model  = SelfAttention({
  "dmodel":  768, 
  "dkey":   128, 
  "dvocab":    4096
})
 
 # Inputs to the model