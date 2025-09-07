
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.randn(1)

    def forward(self, query, key, value):

        v1  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1) 
        v4  = v3.dropout(p=0.5)
        __output__  = value.matmul(v4, beta=2.) # Compute the dot product of the dropout output and the value tensor

        return v4


# Initializing the model:
model  = Model()

# Inputs to the model: