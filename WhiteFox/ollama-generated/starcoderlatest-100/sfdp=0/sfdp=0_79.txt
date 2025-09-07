
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(32, 64)
        self.query = torch.nn.Linear(32, 64)
        self.value = torch.nn.Linear(32, 64)
 
    def forward(self, x):
        scaled_dot_product = torch.matmul(self.query(x), self.key(x).transpose(-2, -1)) / math.sqrt(float(x.shape[0]))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(self.value(x))
        return output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(5, 32, 64)
