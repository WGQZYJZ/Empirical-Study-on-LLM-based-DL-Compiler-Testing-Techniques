
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 512)
        self.key   = torch.nn.Linear(256, 512)
        self.value = torch.nn.Linear(256, 512)
 
    def forward(self, query):
        qk    = torch.matmul(query, self.key.transpose(-2, -1)) * scale_factor # Scale the dot product by a factor
        softmax_qk = torch.softmax(qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = torch.matmul(dropout_qk, self.value)
        return output


# Initializing the model
m = Model()
