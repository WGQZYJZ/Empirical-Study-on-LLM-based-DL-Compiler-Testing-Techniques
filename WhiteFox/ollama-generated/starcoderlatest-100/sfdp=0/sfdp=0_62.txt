
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(160, 84)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / (0.5 ** 0.5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 320, 56, 56)
x2 = torch.randn(84, 320, 56, 56)
