
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):  # Two input tensors
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(torch.randn(*scaled_dot_product.size()))
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 4, 8) # input tensors with shape [batch size (N), length of query/key vectors (H), dimensionality of query/key vectors (D)]
x2  = torch.randn(3, 64, 8)


