
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.randn((1, 1))
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / torch.tensor(0.5) # Scale the dot product by a constant value of `0.5`
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2) # Apply dropout to the softmax output with a dropout probability of `0.2`
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m  = Model()


# Inputs to the model