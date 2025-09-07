
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax  = torch.nn.Softmax(-1)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query and a key tensor
        scaled_qk  = qk / math.sqrt(key.size(-1))# Scale the dot product by `scale_factor`
        softmax_qk  = self.softmax(scaled_qk)  # Apply Softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout with probability 0.5 
        output  = dropout_qk @ value  # Compute the dot product of the dropout output and a value tensor 
        return output

# Initializing the model
m  = Model()

