
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(
            embed_dim=8, 
            num_heads=4)
 
    def forward(self, x1, x2, scale):
        attention_weights  = self.att(x1, x2, x2)[0] # This returns the output of MultiheadAttention, which contains the weights for each heads as well as a vector for each head
        scaled_dot_product = torch.matmul(attention_weights, x2) / scale
        output = scaled_dot_product.transpose(-2, -1).reshape(scaled_dot_product.shape[0], attention_weights.shape[-2] * attention_weights.shape[-1])  # This performs the last linear transformation of the query tensor to get the final representation
        return output


# Initializing the model
m = Model()
scale = math.sqrt(3)

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64) # batch size x seq_len x dim x dim
x2 = torch.randn(1, 32, 8, 64)   # batch size x num heads x n_heads x dim x dim
       
