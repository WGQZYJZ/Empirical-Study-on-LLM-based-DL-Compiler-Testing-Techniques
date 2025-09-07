
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1.mul(scale_factor)
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        v5  = v4.matmul(value)
        return v5


# Initializing the model
m = Model()

 # Inputs to the model