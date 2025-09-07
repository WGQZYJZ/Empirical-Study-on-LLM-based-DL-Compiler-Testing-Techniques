
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # compute the dot product of the query and the key
        scaled_qk = qk / math.sqrt(x1.size(-1) * x2.size(-1))  # scale the dot product by the inverse of the dimension of each matrix
        softmax_qk = scaled_qk.softmax(dim=-1) # apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.25)  # apply dropout to the softmax output
        output = self.linear(dropout_qk.matmul(x2)) # compute the dot product of the dropout output and the key
        return output


# Initializing the model
m = Model()

