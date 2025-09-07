
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(16, 256)
        self.query = torch.nn.Linear(16, 256)
 
    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 80, 256) # The batch size of query is fixed at 1 because there are only two queries in each example
key = torch.randn(1, 4096, 256) # The dimension of key tensor can be any value you want
value = torch.randn(1, 80, 256) # The batch size of query is fixed at 1 because there are only two queries in each example
inv_scale_factor = 0.00390625 # Scale factor for softmax function
dropout_p = 0.4 # Dropout probability to be applied


