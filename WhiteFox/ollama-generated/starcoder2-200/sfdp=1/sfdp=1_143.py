
class MyModel(torch.nn.Module):
    def __init__(self, inv_scale_factor=1., dropout_p=0.)
        super().__init__()
        self.qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        self.softmax_qk = self.qk.div(inv_scale_factor).softmax(dim=-1)  # Apply softmax to the scaled dot product
        self.dropout = torch.nn.functional.dropout(self.softmax_qk, p=dropout_p) # Apply dropout to the softmax output
 
    def forward(self, query):
       return self.qk(query).div(inv_scale_factor).softmax(dim=-1))

# Initializing the model
m = MyModel()


