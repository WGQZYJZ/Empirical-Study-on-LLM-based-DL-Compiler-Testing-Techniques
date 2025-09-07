
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.attention_head = torch.nn.ModuleList()
        for _ in range(num_heads):
            self.attention_head.append(
                torch.nn.Linear(8, 32)
            )
 
    def forward(self, x1, x2):
        v1 = []
        for i in range(self.num_heads):
            attention_output = self.attention_head[i](x1).squeeze()
            v1.append(attention_output)
        query = torch.stack(v1, dim=0)

        scaled_dot_product = torch.matmul(query, x2.transpose(-2, -1)) / (self.inv_scale ** 0.5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        
        v2 = []
        for i in range(self.num_heads):
            value_output = self.attention_head[i](x2).squeeze()
            v2.append(value_output)
        value = torch.stack(v2, dim=0)

        output  = attention_weights.matmul(value)
        
        return output
# Initializing the model
m = MultiHeadAttention(8)


def make_model():
    return Model()
# Inputs to the model
x1 = torch.randn(64, 3, 64, 64)
x2 = torch.randn(64, 8, 64, 64)
