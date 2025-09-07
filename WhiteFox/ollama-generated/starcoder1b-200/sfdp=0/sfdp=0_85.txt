
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query = self.conv(x1)
        key   = self.conv(x2)
        scale = torch.sqrt(torch.max(query.size(2), key.size(2)))
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()


