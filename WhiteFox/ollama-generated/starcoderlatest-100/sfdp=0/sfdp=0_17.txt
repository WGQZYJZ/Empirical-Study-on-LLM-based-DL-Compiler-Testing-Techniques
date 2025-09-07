
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.projection = torch.nn.Linear(768, 3072)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(float(x1.shape[-1]))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)

        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 768, 500, 43)
key = torch.randn(1, 768, 500, 43)
