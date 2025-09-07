

class Model(torch.nn.Module):
    def __init__(self, inv_scale=64037528199):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / \
            (inv_scale ** 0.5) # Divide by the square root of the inv_scale factor
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model 
query = torch.randn(8, 32074) # a randomly generated query vector (assuming 64k is enough)
key = torch.randn(8, 1594, 32074) # a randomly generated key vector that matches the first dimension of the query tensor 
                                  # assuming 64k is enough to make this work for 8 BPE segments and 400 batch size
value = torch.randn(8, 1594, 32074) # a randomly generated value vector that matches the shape of key/query vectors
                                   # but with 3B+ batch size. If 64K is not enough to make this work for 
                                  # 8 BPE segments and 400 batch size, 10x that number (i.e., 256k) should be more than enough.

