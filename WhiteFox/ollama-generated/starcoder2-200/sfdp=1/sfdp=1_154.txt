
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key)
        v2  = v1 / self._scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=self._dropout_p)
        v5  = dropout_qk.matmul(value) 
        return v5

m  = Model()
inv_scale_factor  = 8.0 # An arbitrary constant used in the dot product
m._scale_factor   = inv_scale_factor  # Use this constant to initialize the constant that will be used as an argument for the division operation inside the model's forward method
p  = 1e-3 # An arbitrary dropout probability, used to apply dropout when computing the softmax
m._dropout_p      = p

