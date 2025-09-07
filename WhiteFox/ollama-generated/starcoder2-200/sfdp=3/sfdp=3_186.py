
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1):
        qk = torch.matmul(query1, key1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scale_factor = 0.5 / math.sqrt(qk)
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.4)
        output = dropout_qk.matmul(value1)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
 
