
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Embedding(50265, 512)
 
    def forward(self, x1):
        v1 = torch.matmul(x1, self.key) / math.sqrt(v.shape[1])
        return v

# Initializing the model
m = Model()

 # Inputs to the model
query_embedding  = torch.randn(4096, 50265, dtype=torch.float32)
key_embedding  = torch.randn(4096, 512, dtype=torch.float32)
value_tensor  = torch.randn(128, 512, dtype=torch.float32)

 # Inputs to the model
