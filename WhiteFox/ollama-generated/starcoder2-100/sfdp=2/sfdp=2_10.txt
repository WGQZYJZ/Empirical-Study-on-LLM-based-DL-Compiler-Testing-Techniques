
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qry, ky, vlue):
        v1 = torch.matmul(qry, ky.transpose(-2, -1))  # Compute the dot product of a query and a key
        inv_scale = qrt.mean(v1.abs().max(), dim=-1)
        v2 = v1 / scale_factor
        v3 = torch.nn.functional.softmax(v2, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(v3, p=dropout_p)  # Apply dropout to the softmax output
        v4  = dropout_qk @ value  # Compute the dot product of the dropout output and a value
        return v4


# Initializing the model<|end_of_model|>
m  = Model()
 
# Inputs to the model
query, key, value = torch.randn(128, 64), torch.randn(128, 3072, 64), torch.randn(128, 900, 5)

