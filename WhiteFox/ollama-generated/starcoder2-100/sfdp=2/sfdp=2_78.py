class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(32, 768)
        self.key = torch.randn(32, 768) 
        self.value = torch.randn(32, 1024)
 
    def forward(self, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(scale_factor) # Compute the dot product of the query and the key
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  
        output = dropout_qk.matmul(value) 
        return output
