
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.tensor([0.5]))
        self.att  = torch.nn.MultiheadAttention(embed_dim=64, num_heads=2)
 
    def forward(self, q1, k1, v1):
        qv1  = torch.matmul(q1, v1.transpose(-2, -1)) * self.scale  # Compute the dot product of the query and value tensors
        skv1  = qv1.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(skv1, p=0.5)  # Apply dropout to the softmax output
        return dropout_qk @ k1
 
# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn([32, 64])
key  = torch.randn(32, 64)
value  = torch.randn([32, 64])

__output__  = m(query, key, value)