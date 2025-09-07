
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.tensor([2048])
        self.dropout = 1e-5
 
    def forward(self, query, key, value): 
        qk = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and the key
        scaled_qk = qk / math.sqrt(self.scale)   # Scale the dot product by 2048^(1/2) to achieve normalization
        softmax_qk = torch.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout)   # Apply dropout to the softmax output and obtain the dropout output
        output  = dropout_qk.matmul(value)    # Compute the dot product of the dropout output and a value
        return output
# Initializing the model
m  = Model()

