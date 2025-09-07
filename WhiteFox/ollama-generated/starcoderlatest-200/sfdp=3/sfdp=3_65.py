
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_head = torch.nn.Linear(40, 60)
 
    def forward(self, q1, k1, v1):
        scaled_qk = torch.matmul(q1, k1.transpose(-2, -1)) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.attn_head(softmax_qk).matmul(v1)
        output = dropout_qk
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(4, 20, 30, 50)
k1 = torch.randn(8, 60, 72, 90)
v1 = torch.randn(8, 60, 72, 90)
