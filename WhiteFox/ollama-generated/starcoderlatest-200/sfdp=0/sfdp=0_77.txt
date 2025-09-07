
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 1024) # Linear projection head for queries
        self.key = torch.nn.Linear(768, 1024)    # Linear projection head for keys
        self.value = torch.nn.Linear(768, 1024)   # Linear projection head for values

    def forward(self, x1):
        q1 = self.query(x1)
        k1 = self.key(x1)
        v1 = self.value(x1)
        scaled_dot_product = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(k1.shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 512, 1000, 48).cuda() # N * C * L * D -> B * T * H * W
