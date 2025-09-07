
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scale_factor = qk.max().detach() * 0.3
        scaled_qk = qk / scale_factor  # Scale the dot product by the scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output
        ouput = dropout_qk.matmul(value)
        return ouput


# Initializing the model
m = Model()


# Inputs to the model