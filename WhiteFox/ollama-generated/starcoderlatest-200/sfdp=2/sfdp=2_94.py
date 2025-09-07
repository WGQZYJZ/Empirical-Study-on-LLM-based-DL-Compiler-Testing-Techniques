
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(4096, 4096)
        self.key = torch.nn.Linear(4096, 4096)
        self.value = torch.nn.Linear(4096, 4096)
 
    def forward(self, query):
        key = self.key(query)
        value = self.value(query)
 
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk.div(inv_scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value) 
        return output


# Inputs to the model
query = torch.randn(4096, 256, 100, 784)
