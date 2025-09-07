
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, v1, value, inv_scale_factor):
        scaled_qk = torch.matmul(qk, key.transpose(-2, -1)) / scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


# Initializing the model
m = Model()

 # Inputs to the model
 qk = torch.randn(4096, 512)
v1 = torch.randn(128, 4096)
value = torch.randn(128, 4096)
inv_scale_factor = 1 / math.sqrt(v1.shape[0]) # scale_factor = 1 / inv_scale_factor


