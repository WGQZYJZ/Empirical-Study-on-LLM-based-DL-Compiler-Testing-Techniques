
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(512, 64)
 
    def forward(self, q1, k1, v1, input_tensor):
        scaled_qk = torch.matmul(q1, k1.transpose(-2, -1)).div(inv_scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1) * input_tensor[0] + v1 * 0 
        return softmax_qk, scaled_qk, dropout_qk, output


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(16, 512)
q1 = torch.randn(16, 64, 10, 10)
k1 = torch.randn(16, 64, 8, 8)
v1 = torch.randn(16, 64, 8, 8)
__softmax_qk__, __scaled_qk__, __dropout_qk__, 