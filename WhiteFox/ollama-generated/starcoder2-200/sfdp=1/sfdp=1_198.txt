
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.scale = 1e4
        self.inv_scale = float(1 / scale)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        v0 = torch.matmul(query, key.transpose(-2, -1))
        v1 = v0 * inv_scale_factor # Scale the dot product by an inverse scale factor
        v2 = v1.softmax(dim=-1) 
        v3 = torch.nn.functional.dropout(v2, p=dropout_p) 
        v4 = v3.matmul(value)
 
        return v4


# Initializing model
m  = Model()
 
__output__  = m(torch.randn(10), torch.randn(10, 10), torch.randn(10, 10)) # Inputs to the model
 
