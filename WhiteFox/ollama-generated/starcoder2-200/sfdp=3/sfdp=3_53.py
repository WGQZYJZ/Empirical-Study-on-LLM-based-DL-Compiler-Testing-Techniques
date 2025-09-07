
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1 = torch.matmul(query1, 
                          key2.transpose(-2, -1))
        v2 = v1 * scale_factor 
        v4 = v2.softmax(dim=-1)
        v5 = torch.nn.functional.dropout(v4, p=dropout_p)
        v6 = v5.matmul(value3) # Compute the dot product of the dropout output and the value tensor
        return v6

# Initializing the model
m  = Model()


# Inputs to the model
k21  = torch.randn(10, 9)
k22  = torch.randn(345, 78)
v1_2  = torch.randn(10, 78) # This is a query tensor
v21  = torch.randn(78, 3)
v22  = torch.randn(9, 67)
v3   = torch.randn(9, 54)

 