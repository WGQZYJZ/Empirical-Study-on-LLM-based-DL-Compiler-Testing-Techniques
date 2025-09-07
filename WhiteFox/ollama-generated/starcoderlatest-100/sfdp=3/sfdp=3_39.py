
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.Linear(10, 8)
 
    def forward(self, x1, x2):
        v1 = self.attention_layer(x1)
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1).unsqueeze(-2)  # Add a dimension to the result tensor of matmul() and unsqueeze() with size (-1,) 
        return output
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 32, 64, 64)
