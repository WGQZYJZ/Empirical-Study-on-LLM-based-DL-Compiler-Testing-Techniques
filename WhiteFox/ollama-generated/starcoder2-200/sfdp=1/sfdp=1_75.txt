
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        qk = torch.matmul(x1[0], x1[1].transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output  = dropout_qk.matmul(x1[2]) 
        return output


# Initializing the model
m  = Model()

# Inputs to the model
inputs  = [torch.randn(32, 50), torch.randn(32, 48)]
__output__  = m(inputs)


