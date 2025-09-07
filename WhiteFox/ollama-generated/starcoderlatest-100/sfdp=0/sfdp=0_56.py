
class Model(torch.nn.Module):
    def __init__(self, dim=256):
        super().__init__()
        self.attention_head = torch.nn.Sequential(
            torch.nn.Linear(dim, dim),
            torch.nn.Softmax(),
            torch.nn.Linear(dim, 1)
        )
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.shape[-1])
        attention_weights = self.attention_head(scaled_dot_product).unsqueeze(-1)
        return attention_weights.bmm(value)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
