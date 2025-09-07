
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1  = torch.matmul(query1, key2.transpose(-2, -1))
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        v5  = v4.matmul(value3)
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
query1  = torch.randn(20, 768)
key2   = torch.randn(20, 768)
value3 = torch.randn(20, 768)
__output__  = m(query1, key2, value3)

