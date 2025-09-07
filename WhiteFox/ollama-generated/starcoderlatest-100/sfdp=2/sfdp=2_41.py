
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 512)
 
    def forward(self, x1, x2):
        v1 = self.query(x1)
        scaled_qk = torch.matmul(v1, x2.transpose(-2, -1)) * inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output


# Initializing the model
m = Model()

 # Inputs to the model
q1 = torch.randn(16, 1024, 512)
k1 = torch.randn(16, 512, 1024)
v1 = torch.randn(16, 512, 1024)
