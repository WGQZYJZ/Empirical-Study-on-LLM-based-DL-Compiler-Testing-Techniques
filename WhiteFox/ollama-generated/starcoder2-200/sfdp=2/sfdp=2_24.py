
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, inv_scale_factor=1.0, dropout_p = 0.5):
        v1  = torch.matmul(q, k.transpose(-2,-1))
        v2  = v1 / inv_scale_factor
        v3  = v2.softmax(-1)
        v4  = nn.functional.dropout(v3, p=dropout_p)
        v5  = v4 @ v

# Initializing the model