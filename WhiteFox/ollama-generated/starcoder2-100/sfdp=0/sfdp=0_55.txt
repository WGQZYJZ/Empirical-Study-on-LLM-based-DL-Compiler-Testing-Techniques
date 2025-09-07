
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        # Replace the dot product with another operation
        scaled_dot_product = torch.einsum("...ij,...jk->...ik", x1, x2) / 8
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        output  = attention_weights.matmul(x2)
        
        return output


# Initializing the model
m  = Model()
 
 # Inputs to the model
 
x1  = torch.randn(5,4)
x2  = torch.randn(5,8)

  __output__  = m(x1, x2)
