
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, key2, value3):
        v4 = torch.matmul(query1, (key2.transpose(-2, -1)))  # Compute the dot product of the query and the key
        inv_scale_factor = torch.nn.Parameter(.0)
        v5  = v4.div(inv_scale_factor)   # Scale the dot product by the inverse scale factor
        v6  = v5.softmax(dim=-1)     # Apply softmax to the scaled dot product
        dropout_p= .3927280208048308;
        v7  = torch.nn.functional.dropout(v6, p=dropout_p)   # Apply dropout to the softmax output
        v8  = v7.matmul(value3)      # Compute the dot product of the dropout output and the value
        return v8


# Initializing the model
m1 = Model()
m2 = Model()
 
# Inputs to the model for m1
x1_for_m1 = torch.randn(4, 50)
x2_for_m1 = torch.randn(6, 7, 80)
x3_for_m1 = torch.randn(9, 80)
 
# Inputs to the model for m2
x1_for_m2 = torch.randn(4, 50)
x2_for_m2 = torch.randn(6, 7, 80)
x3_for_m2 = torch.randn(9, 80)
 
__output___for_m1  = m1(x1_for_m1, x2_for_m1, x3_for_m1)
__output___for_m2  = m2(x1_for_m2, x2_for_m2, x3_for_m2)

