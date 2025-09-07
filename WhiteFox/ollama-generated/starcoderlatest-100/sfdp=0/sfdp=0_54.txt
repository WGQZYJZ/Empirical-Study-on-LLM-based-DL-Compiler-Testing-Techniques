
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(32, 64)
        self.value = torch.nn.Linear(64, 64)
        self.query = torch.nn.Linear(128, 32)
 
    def forward(self, x):
        scaled_dot_product = torch.matmul(x, self.key.weight.transpose(-2, -1)) / (10 ** 5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(self.value.weight)
        return output


# Initializing the model
m = AttentionModel()

# Inputs to the model
x1 = torch.randn(4, 32, 64)
