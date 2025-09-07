
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(3072, 64)
        self.linear_k = torch.nn.Linear(192, 64)
        self.linear_v = torch.nn.Linear(192, 64)
 
    def forward(self, q, k, v):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(v.shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3072, 64)
