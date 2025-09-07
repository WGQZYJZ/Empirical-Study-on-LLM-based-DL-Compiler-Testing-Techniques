
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 * scale_factor
        v3  = scaled_qk.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v5  = dropout_qk.matmul(value)

# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(1024, 768)
key    = torch.randn(1024, 768)
value  = torch.randn(768, 512)
 
