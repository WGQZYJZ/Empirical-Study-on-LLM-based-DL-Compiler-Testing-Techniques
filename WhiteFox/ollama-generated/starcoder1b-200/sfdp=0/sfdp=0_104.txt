
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.norm1 = torch.nn.LayerNorm((8,))
 
    def forward(self, x1):
        norm1 = self.norm1(x1)
        v1 = self.conv1(norm1)
        scaled_dot_product = torch.matmul(v1, v1.transpose(-2, -1)) / math.sqrt(8)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x1)
        return output


# Initializing the model
m  = Model()
