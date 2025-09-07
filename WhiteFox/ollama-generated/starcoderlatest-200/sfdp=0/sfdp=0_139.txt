
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(data=torch.randn((1024, 65536)), requires_grad=True)
        self.query = torch.nn.Parameter(data=torch.randn((1024, 65536)), requires_grad=True)
 
    def forward(self, key):
        scaled_dot_product = torch.matmul(self.query, key.transpose(-2, -1)) / np.sqrt(key.shape[0])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(self.value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(2, 3, 64, 64)
