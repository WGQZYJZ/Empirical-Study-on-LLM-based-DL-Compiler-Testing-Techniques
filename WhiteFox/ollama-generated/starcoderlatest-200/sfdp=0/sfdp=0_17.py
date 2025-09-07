
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(768, 3072)
        self.layer_norm1 = torch.nn.LayerNorm([768])
 
    def forward(self, x1):
        query = self.layer_norm1(x1)
        key = torch.transpose(query, -2, -1)
        attention_weights  = torch.matmul(query, key) / math.sqrt(2048)
 
        output = attention_weights.matmul(key)
        return output
 
 
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(5, 768, 256, 256)
