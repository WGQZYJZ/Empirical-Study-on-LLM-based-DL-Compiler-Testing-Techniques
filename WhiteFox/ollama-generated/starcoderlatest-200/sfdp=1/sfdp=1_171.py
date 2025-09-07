
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 128)
        self.key = torch.nn.Linear(1024, 128)
        self.value = torch.nn.Linear(1024, 128)
 
    def forward(self, query_tensor, key_tensor, value_tensor):
        qk = torch.matmul(query_tensor, key_tensor.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value_tensor)
        return output


# Inputs to the model
query_tensor = torch.randn(16, 1024)
key_tensor = torch.randn(32, 1024)
value_tensor = torch.randn(32, 1024)
