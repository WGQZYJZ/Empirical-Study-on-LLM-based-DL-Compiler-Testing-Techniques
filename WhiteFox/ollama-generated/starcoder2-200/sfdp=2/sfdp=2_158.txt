
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v0 = torch.matmul(query1, key2)  # Compute the dot product of a query and a key
        scaled_v0 = v0 / inv_scale_factor  # Scale the dot product by an inverse scale factor
        softmax_v0 = scaled_v0.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_v0 = torch.nn.functional.dropout(softmax_v0, p=dropout_p)  # Apply dropout to the softmax output
        v1 = dropout_v0.matmul(value3)
        return v1
# Initializing the model
m  = Model()


# Inputs to the model
query1  = torch.randn(256, 256).cuda()  # Input tensor for query in the 1st layer of Transformer models
key2   = torch.randn(256, 256)         .cuda()  # Input tensor for key in the 1st layer of Transformer models
value3 = torch.randn(256, 256).cuda()       # Input tensor for value in the 1st layer of Transformer models


__output__  = m(query1, key2, value3)


