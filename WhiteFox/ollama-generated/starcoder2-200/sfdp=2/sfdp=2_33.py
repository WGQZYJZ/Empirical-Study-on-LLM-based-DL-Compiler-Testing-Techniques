
class Model(torch.nn.Module):
    def __init__(self, d_model=64, dropout_p=0.1):
        super().__init__()
        self.scale = torch.rsqrt(torch.tensor([d_model]))
        self.dropout  = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and the key
        v3 = self.dropout(v1.div_(self.scale)) # Apply dropout to the scaled dot product by using scale parameter.
        v4  = v3.softmax(dim=-1) # Apply softmax to the scaled dot product
        return v4.matmul(value)


# Initializing the model<|end_of_model|>
d_model = 64
dropout_p = 0.1
m = Model(d_model, dropout_p)

# Inputs to the model (query/key/value)
query  = torch.randn([256, d_model])
key    = torch.randn([256, d_model])
value  = torch.randn([256, 10])

