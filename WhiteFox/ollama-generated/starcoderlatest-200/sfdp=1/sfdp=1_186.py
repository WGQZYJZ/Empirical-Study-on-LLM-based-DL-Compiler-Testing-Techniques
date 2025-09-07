
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_linear = torch.nn.Linear(128, 512)
        self.k_linear = torch.nn.Linear(128, 512)
        self.v_linear = torch.nn.Linear(128, 512)
 
    def forward(self, x1, x2):
        query = self.q_linear(x1)
        key = self.k_linear(x2)
        value = self.v_linear(x2)
 
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 256, 128, 128)
x2 = torch.randn(16, 256, 32, 32)
