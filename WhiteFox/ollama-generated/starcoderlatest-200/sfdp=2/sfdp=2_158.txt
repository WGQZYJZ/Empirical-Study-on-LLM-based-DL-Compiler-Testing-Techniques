
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_qk = torch.nn.Linear(512, 512)
 
    def forward(self, query, key, value, inv_scale_factor=None):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output
# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(batch_size, 512, input_resolution, input_resolution)
key = torch.randn(batch_size, 512, input_resolution, input_resolution)
value = torch.randn(batch_size, 512, input_resolution, input_resolution)
