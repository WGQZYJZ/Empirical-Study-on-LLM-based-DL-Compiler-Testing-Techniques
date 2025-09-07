
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(128, 1)
 
    def forward(self, x1, key):
        scaled_dot_product = torch.matmul(x1, key.transpose(-2, -1)) / math.sqrt(32 * 64)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x1)
        return output


# Initializing the model
m = Model()
m = m.eval()


