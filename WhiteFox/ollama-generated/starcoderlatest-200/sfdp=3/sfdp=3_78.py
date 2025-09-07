
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w_query = torch.nn.Linear(768, 30528)
        self.w_key = torch.nn.Linear(768, 30528)
        self.w_value = torch.nn.Linear(768, 30528)
        self.attention = None
 
    def forward(self, query, key, value):
        scaled_qk = torch.matmul(query, self.w_key.weight).transpose(-2, -1).div(math.sqrt(self.w_key.in_features))  # Compute the dot product of the query and key tensors
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        output = torch.matmul(softmax_qk, self.w_value.weight).transpose(-2, -1)  # Compute the dot product of the dropout output and the value tensor
        return output
 
