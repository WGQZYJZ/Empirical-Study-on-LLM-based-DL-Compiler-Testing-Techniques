
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        inv_scale = torch.sqrt(query.shape[-1])  # Assume the dimension of key/value is 8x32
        scaled_dot_product = torch.matmul(
            query / inv_scale, key.transpose(-2, -1)
        )
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights @ value
        return output


# Initializing the model
m  = Model()
# Inputs to the model: query and key tensors that are different from previous one
q = torch.randn(32, 64, 8)
k = torch.randn(32, 1024, 32).transpose(-2, -1)
v = torch.randn(32, 1024, 576)


# Initializing the previous model: it will be used as a baseline in order to compare with the newly generated model
m_old  = Model()
q_old = torch.randn(32, 64, 8)
k_old = torch.randn(32, 1024, 32).transpose(-2, -1)


# Compute the output of the previous model for the input query and key tensors: q is different from m_old's input tensor, k is also a different tensor compared to m_old'input tensor.
__output___  = m_old(q, k, v).shape
assert __output___[0] == 32

