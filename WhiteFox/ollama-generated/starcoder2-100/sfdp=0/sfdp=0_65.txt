
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        scaled_dot_product  = torch.matmul(q1, k1) / sqrt(torch.tensor(k1).size(-1))
        attention_weights  = scaled_dot_product.softmax(dim=-1) # scaled dot product is added
        output  =  q2 * k3 * v4 # addition is performed
        return output


# Initializing the model:

m  = Model()


# Inputs to the model

q1  = torch.randn(10, 16) # 10 sequences of length 16 with elements in R^32
k1  = torch.randn(48, 16, 32) # 48 embedding matrices of size (16x32)
v1  = torch.randn(48, 16, 32)


__output__  = m(q1, k1, v1).sum()

