
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v3  = inv_scale_factor * v1
        v4  = torch.nn.functional.softmax(v3)
        v5  = torch.nn.functional.dropout(v4, p=dropout_p)
        return value @ v5


# Initializing the model