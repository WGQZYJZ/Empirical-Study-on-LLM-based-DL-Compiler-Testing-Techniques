
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(8192, 512)
 
    def forward(self, qk, value):
        scaled_qk = self.qk(qk).mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk  = torch.randn(4, 8192, 512) # 4 is the number of heads
value  = torch.randn(4, 3072, 512) # 4 is the number of heads
