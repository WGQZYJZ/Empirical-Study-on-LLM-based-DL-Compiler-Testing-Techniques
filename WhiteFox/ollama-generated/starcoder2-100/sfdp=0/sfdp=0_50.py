
class TransformerAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding  = torch.nn.Embedding(200, 768)
 
    def forward(self, query, key, value): 
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return self.embedding(output), attention_weights

# Initializing the model
m  = TransformerAttention()

 # Inputs to the model
x1, x2, x3  = torch.randn((1024, 768)), torch.randn((1024, 512, 768)), torch.randn((1024, 512, 768))
__output__,  __attentions_weights__  = m(x1, x2, x3)

