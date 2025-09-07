
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 384) 
        self.key   = torch.nn.Linear(512, 384) 
        self.value = torch.nn.Linear(384, 768)
 
    def forward(self, q):
        k, v = self.query(q), self.value(q)
        scaled_dot_product = torch.matmul(k, v.transpose(-2, -1)) / math.sqrt(v.size(-1))
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
q = torch.randn(2, 384, 512)
