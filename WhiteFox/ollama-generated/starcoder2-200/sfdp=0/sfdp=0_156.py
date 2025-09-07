
class DotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output
 
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1  = torch.nn.Linear(5, 30)
        self.dropout = torch.nn.Dropout()
        self.dot_product_attention = DotProductAttention()
        self.layer2  = torch.nn.Linear(30, 10)
 
    def forward(self, x): 
        output = self.layer1(x).relu_()
 
        output = self.dropout(output)
        output = self.layer2(output).relu_()
        return output

# Initializing the model
m = AttentionModel()

 # Inputs to the model
x  = torch.randn(5, 60)
 
__outputs1__ = m(x)

