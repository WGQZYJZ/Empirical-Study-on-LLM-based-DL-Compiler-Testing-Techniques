
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 0.5713684922330329
 
    def forward(self, query, key, value):
        scale_factor = torch.full((query.size(-1), ), self.scale)
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk * scale_factor  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.28965747314040655) 
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output

m = Model()

