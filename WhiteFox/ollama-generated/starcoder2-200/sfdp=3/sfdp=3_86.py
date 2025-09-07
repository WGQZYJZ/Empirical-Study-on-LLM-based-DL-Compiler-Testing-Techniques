
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.tensor([float(1/math.sqrt(d))])
 
    def forward(self, query, key, value):
        scaled_query  = query * self.scale
        scaled_qk  = torch.matmul(scaled_query, key)
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output  = dropout_qk.matmul(value)
        return output


# Initializing the model
scaled_dot_product_attention = ScaledDotProductAttention()
scaled_dot_product_attention.scale = torch.tensor([float(64/75)]) # Change the scale value of scaled dot product attention


# Inputs to the model 
query1  = torch.randn(3, 32)
key1  = torch.randn(3, 30)
value1  = torch.randn(3, 64)

query2  = torch.randn(75, 32)
key2  = torch.randn(32, 30)
value2  = torch.randn(75, 64)
 

