
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        scaled_dot_product  = torch.matmul(query1, key2.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        output = attention_weights.matmul(value3)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(5, 2048, 768)
x2 = torch.randn(5, 2048, 768)
x3 = torch.randn(5, 768, 19)

 # Model output produced by the model
__output__  = m(x1, x2, x3)
