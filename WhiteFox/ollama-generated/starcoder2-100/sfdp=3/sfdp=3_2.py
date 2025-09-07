
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, key1, value1):

        query2 = torch.randn(3)
        key2 = torch.randn(4)
        value2 = torch.randn(5)
        v1  = torch.matmul(query1, key1.transpose(-2, -1))
        v1 = v1 * scale_factor
        v1  = v1 .softmax(dim=-1) 
        v1  = v1.dropout(p=dropout_p) 
        v1  = v1.matmul(value1) 

        v2  = torch.matmul(query2, key2.transpose(-2, -1))
        v2 = v2 * scale_factor
        v2  = v2 .softmax(dim=-1) 
        v2  = v2.dropout(p=dropout_p) 
        v2  = v2.matmul(value2)

        return (v1 + v2), torch.cat((value1, value2), dim=-3).permute(-2,-4,-3), query1.add_(query2)

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(5,6)
x2  = torch.randn(7,8)

# Parameters for dropout and scaling factor
dropout_p  = 0.3
scale_factor  = 4.3e-3

 __output__  = m(x1, x2)

