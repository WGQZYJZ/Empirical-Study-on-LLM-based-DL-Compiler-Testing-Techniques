
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk1):
        query, key = qk1
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) * scale_factor 
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk1 = (torch.randn(1, 3, 64, 64), torch.randn(1, 3, 64, 64))
