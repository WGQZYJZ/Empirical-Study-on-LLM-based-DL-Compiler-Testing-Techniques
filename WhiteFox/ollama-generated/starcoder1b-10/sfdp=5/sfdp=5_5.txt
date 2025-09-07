
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 10)
 
    def forward(self, x1, x2):
        k1 = self.attn(x1).unsqueeze(-1) # Get the keys of the linear layer at index 768
        k2 = self.attn(x2).unsqueeze(-1) # Get the keys of the linear layer at index 768
        query  = torch.matmul(k1, k2).squeeze(-1)  # Multiply the keys with values in a 2-D matrix, to obtain a vector (query size N x D), where query[i] is the dot product of key[i] and value[i].
        return self.attn(x1 + x2) * query  # Apply the dot product with the attention weights computed by the softmax


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 768)
x2 = torch.randn(3, 768)
