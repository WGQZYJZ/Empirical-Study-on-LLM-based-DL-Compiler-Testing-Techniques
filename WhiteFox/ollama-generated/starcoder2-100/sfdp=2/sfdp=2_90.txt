
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q1):
        v1  = torch.matmul(q1[:, None], self.key) # Compute the dot product of the query and key
        v2  = v1 / (3e-5 + v1.std(-1))[:, None] # Scale the dot product by an inverse scale factor
        v3  = v2.softmax(dim=-1).dropout(p=0.5) # Apply dropout to the softmax output
        return torch.matmul(v3, self.value)

# Initializing the model
m  = Model()


# Inputs to the model
k1 = torch.randn([8*7, 32])
v1 = torch.randn([32, 500 * 64 * 64])
x1 = torch.randn(4, 32, 1) # query size of batch 4, dim=32


# Setting up the model
m.key, m.value  = k1, v1
 
__output__  = m(q1).argmax(-1) 

