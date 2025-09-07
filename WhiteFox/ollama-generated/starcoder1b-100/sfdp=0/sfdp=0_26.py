
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.scale_key  = torch.sqrt(torch.FloatTensor([10]))
 
    def forward(self, x1):
        scaled_dot_product = torch.matmul(x1, self.scale_key.unsqueeze(-2).expand_as(x1))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x1)
        return output


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
